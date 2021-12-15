import sys
import os
my_absolute_dirpath = os.path.abspath(os.path.dirname('BIOINFORMATICS_CLASS'))

from upgma_algorithm import upgma_full

def assert_upgma_full(distance_matrix, labels, true_groupings, true_distances):
    groupings = upgma_full(distance_matrix, labels)['groups']
    distances = upgma_full(distance_matrix, labels)['depths']
    assert groupings == true_groupings
    assert distances == true_distances

def test_upgma_full():
    class_example = [
        [-1, 19, 27, 8, 33, 18, 13],
        [19, -1, 31, 18, 36, 1, 13],
        [27, 31, -1, 26, 41, 32, 29],
        [8, 18, 26, -1, 31, 17, 14],
        [33, 36, 41, 31, -1, 35, 28],
        [18, 1, 32, 17, 35, -1, 12],
        [13, 13, 29, 14, 28, 12, -1]
    ] 
    class_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    true_groupings = [
        ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        ['a', 'bf', 'c', 'd', 'e', 'g'],
        ['ad', 'bf', 'c', 'e', 'g'],
        ['ad', 'bfg', 'c', 'e'],
        ['adbfg', 'c', 'e'],
        ['adbfgc', 'e'],
        ['adbfgce']
    ]
    true_distances = [0, 0.5, 4.0, 6.25, 8.25, 14.5, 17.0]
    assert_upgma_full(class_example, class_labels,)