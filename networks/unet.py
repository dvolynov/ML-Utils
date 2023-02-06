from tensorflow.keras import backend
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras import optimizers



def unet(input_shape, num_classes):
    inputs = layers.Input(shape=input_shape)

    f1, p1 = downsample_block(inputs, 64)
    f2, p2 = downsample_block(p1, 128)
    f3, p3 = downsample_block(p2, 256)
    f4, p4 = downsample_block(p3, 512)

    bottleneck = double_conv_block(p4, 1024)

    u6 = upsample_block(bottleneck, f4, 512)
    u7 = upsample_block(u6, f3, 256)
    u8 = upsample_block(u7, f2, 128)
    u9 = upsample_block(u8, f1, 64)

    outputs = layers.Conv2D(num_classes, (2, 2), padding="same", activation = "softmax")(u9)

    unet_model = models.Model(inputs, outputs, name="U-Net")
    unet_model.compile(
        optimizer=optimizers.Adam(),
        loss='categorical_crossentropy',   
        metrics=[dice_coef]
    )

    return unet_model


def dice_coef(y_true, y_pred):
  return (2. * backend.sum(y_true * y_pred) + 1.) / (backend.sum(y_true) + backend.sum(y_pred) + 1.)


def double_conv_block(x, n_filters):
    x = layers.Conv2D(n_filters, (3, 3), padding='same', activation = "relu")(x)
    x = layers.Conv2D(n_filters, (3, 3), padding='same', activation = "relu")(x)
    return x


def downsample_block(x, n_filters):
    f = double_conv_block(x, n_filters)
    p = layers.MaxPool2D(2)(f)
    p = layers.Dropout(0.3)(p)
    return f, p


def upsample_block(x, conv_features, n_filters):
    x = layers.Conv2DTranspose(n_filters, (2, 2), strides=(2, 2), padding='same')(x)
    x = layers.concatenate([x, conv_features])
    x = layers.Dropout(0.3)(x)
    x = double_conv_block(x, n_filters)
    return x