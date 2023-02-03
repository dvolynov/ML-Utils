# Модули для построения нейросетей на Python 


## Как импортировать в Google Colab

    !rm -rf 'ml'   
    !git clone https://github.com/Ardisat/ml.git   
    from ml.general import split_sample   


## images

    check_batch(sample, names=('x', 'y'))   
    rgb_to_ohe(y, num_classes)   
    smart_trimming(img, size=(100, 100))   

## audio

    get_features(x, sr)