import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def check_batch(sample, names=('x', 'y')):
    x_check, y_check = {}, {}

    for x_batch, y_batch in zip(sample.x_batches, sample.y_batches):
        if not x_check.get(len(x_batch)): x_check[len(x_batch)] = 0
        if not y_check.get(len(y_batch)): y_check[len(y_batch)] = 0

        x_check[len(x_batch)] += 1
        y_check[len(y_batch)] += 1

    radius = 1
    fig, axs = plt.subplots(ncols=2, figsize=(6, 3))
    colors = sns.color_palette("Set2")[0:5]

    for i in range(2):
        check = [x_check, y_check][i - 1]

        data = list(check.values())
        labels = list(check.keys())
        values = list(check.values())
        length = sum(check.values())

        axs[i].pie(data, labels=labels, colors = colors, autopct='', radius=radius)
        axs[i].legend(values, title="Batches", loc="center")

        circle = mpatches.Circle((0, 0), radius=radius*0.8, color='white')
        axs[i].add_patch(circle)

        axs[i].set_title(f"{names[i]}: {length}")

    plt.show()    