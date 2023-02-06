# Модули для построения нейросетей на Python 


## Как импортировать в Google Colab

    !rm -rf 'ml'   
    !git clone -q https://github.com/Ardisat/ml.git   
    from ml.general import split_sample   


## General

    Bar(iterations)
    check_batch(sample, names=('x', 'y'))   
    shuffle_samples(x, y)   
    split_sample(x, y, train=0.7, val=0.2, test=0.1)   

## Images

    check_batch(sample, names=('x', 'y'))   
    rgb_to_ohe(y, num_classes)   
    smart_trimming(img, size=(100, 100))   

## Audio

    get_features(x, sr)

## Video

#### Работа с видео в Google Colab
    video_frame(label, bbox)
    js_to_image(js_reply)
    video_stream()