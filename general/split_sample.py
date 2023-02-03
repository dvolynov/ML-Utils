def split_sample(x, y, train=0.7, val=0.2, test=0.1):
    if len(x) != len(y): raise ValueError('Lengths are not equal')
    if not 0 <= (train+val+test) <= 1: raise ValueError(f'Invalid proportion ({train}|{val}|{test})')

    sample = {'train': {'x': [],'y': []}, 'val':{'x': [],'y': []}, 'test':{'x': [],'y': []}}

    train_coef, val_coef, test_coef = 0, 0, 0
    zip_xy = zip(x, y)
    length = len(x)

    for i, (x_item, y_item) in enumerate(zip_xy):

        if train_coef < train:
            sample['train']['x'].append(x_item)
            sample['train']['y'].append(y_item)
            train_coef = i / length

        elif val_coef < val:
            sample['val']['x'].append(x_item)
            sample['val']['y'].append(y_item)
            val_coef =  (i - len(sample['train']['x'])) / length

        elif test_coef < test:
            sample['test']['x'].append(x_item)
            sample['test']['y'].append(y_item)
            test_coef = (i - len(sample['train']['x']) - len(sample['val']['x'])) / length

    return sample