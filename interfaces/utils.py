from PyQt6.QtGui import QPixmap
import matplotlib.pyplot as plt


def tex2img(formula):
    plt.rc('mathtext', fontset='cm')
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.text(10, 10, r'${}$'.format(formula), fontsize=12)

    fig.savefig('temp.png', dpi=300, transparent=True, format='png',
                bbox_inches='tight', pad_inches=0.1)
    plt.close(fig)

    return QPixmap('./temp.png')
