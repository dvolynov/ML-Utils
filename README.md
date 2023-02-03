# Модули для построения нейросетей на Python 


## Как импортировать в Google Colab

    !rm -rf 'ml'   
    !git clone https://github.com/Ardisat/ml.git   
    from ml.general import split_sample   


## general

    check_batch(sample, names=('x', 'y'))   
    shuffle_samples(x, y)   
    split_sample(x, y, train=0.7, val=0.2, test=0.1)   

## images

    check_batch(sample, names=('x', 'y'))   
    rgb_to_ohe(y, num_classes)   
    smart_trimming(img, size=(100, 100))   

## audio

    get_features(x, sr)