#!/usr/bin/env python

"""Logistic functions applied to image arrays."""


import functools
import numpy

from . import image


def _logistic(k, domain, center, array):
    a, b = domain
    c = center
    return 1.0 / (1.0 + numpy.exp(-k * (b - a) * (array - c)))


def logistic(k, domain, center, img):
    """Apply the logistic function of degree k to an image array."""
    return image.map_to_channels(
        functools.partial(_logistic, k, domain, center),
        lambda shape: shape,
        img,
    )


if __name__ == '__main__':
    pass
