#!/usr/bin/env python3

import sys

from matplotlib.backends.backend_pdf import PdfPages

from mplslide import check_requirements
check_requirements()  # noqa: F402

from title import create_icon_axes, slides as title_slides
from timeline import slides as history_slides
from feature32 import slides as feature32_slides
from feature33 import slides as feature33_slides
from plan import slides as plan_slides


MPL_PATH = sys.argv[1]
PAGES = [
    (title_slides, ),
    (history_slides, MPL_PATH, ),
    (feature32_slides, ),
    (feature33_slides, ),
    (plan_slides, ),
]

with PdfPages('slides.pdf') as pdf:
    for i, (page, *args) in enumerate(PAGES):
        figs = page(*args)
        if not isinstance(figs, (tuple, list)):
            figs = (figs, )
        for fig in figs:
            if i != 0:
                create_icon_axes(fig, (0.825, 0.825, 0.2, 0.15),
                                 0.3, 0.3, 0.3, [5])
            pdf.savefig(fig)
