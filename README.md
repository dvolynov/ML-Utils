# Модули для построения нейросетей на Python 


## Как импортировать в Google Colab

    !rm -rf 'ml'   
    !git clone -q https://github.com/Ardisat/ml.git   
    from ml.general import split_sample   


## General

`Bar(iterations)`   
`check_batch(sample, names=('x', 'y'))`   
`shuffle_samples(x, y)`   
`split_sample(x, y, train=0.7, val=0.2, test=0.1)`   


## Images

`check_batch(sample, names=('x', 'y'))` - вывод графика с информацией о батчах из DataGenerator   
`rgb_to_ohe(y, num_classes)` - перевод numpy картинки в one hot encoding   
`smart_trimming(img, size=(100, 100))` - умная обрезка картинки (с сохранением центра)   


## Audio

`get_features(x, sr)` - получение признаков аудио   


## Video

#### Считывание потока покадрово с камеры в Google Colab
`video_stream()` - захват видео потока   
`video_frame(label, bbox)` - захват кадра из потока   
`js_to_image(js_reply)` - конвертация js картинки в python   

    video_stream()

    while True:
        js_reply = video_frame('Capturing...', '')
        if not js_reply: break

        img = js_to_image(js_reply["img"])