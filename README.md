# Модули Python для Machine Learning


#### Как импортировать в Google Colab

    !rm -rf 'ml'   
    !git clone -q https://github.com/Ardisat/ml.git   
    from ml.general import split_sample   



## Networks

`unet(input_shape, num_classes)` - U-Net



## General

`Bar(iterations)` - прогрессбар для любого цикла   
`check_batch(sample, names=('x', 'y'))` - вывод графика с информацией о батчах из DataGenerator   
`shuffle_samples(x, y)` - перемешивание двух массивов одинаково    
`split_sample(x, y, train=0.7, val=0.2, test=0.1)` - разделение выборки на обучающюю, проверочную и тестовую   



## Images

`rgb_to_ohe(y, num_classes)` - перевод numpy картинки в one hot encoding   
`smart_trimming(img, size=(100, 100))` - умная обрезка картинки (с сохранением центра)   
   


## Audio

`get_features(x, sr)` - получение признаков аудио   
`get_info(track)` - информация о треке   
`text_from_wav(path, language="ru-RU")` - извлечение текста из трека через speech_recognition   
   


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
   