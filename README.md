## Merge-sort Algorithm

We divide the array into two halves, repeatedly splitting it until each segment contains only one element, as single-element arrays are inherently sorted. Then, we merge these segments, comparing elements from each half and arranging them in order. This merging process continues until all segments are combined into a single, sorted array.

## Bubble-sort Algorithm

We start by comparing adjacent elements in the array, checking if the current element is larger than the one next to it. If so, the two components are swapped. This process is repeated for each pair of adjacent elements in the array, effectively 'bubbling' the largest unsorted element to its correct position. The procedure continues for the remaining unsorted portion of the array until the entire array is sorted.

## Insertion-sort Algorithm

We assume the first element of the array is already sorted and begin sorting from the second element. The current element, referred to as the 'key,' is compared to the one before it. If the previous element is larger than the key, they are swapped. This process continues until the key reaches its correct position in the array.

## Quick-sort Algorithm

We first take the pivot as the first element of the array (the middle and the last elements are also viable options). We then iterate through the array, comparing elements to the pivot and partitioning them based on whether they are smaller or larger than the pivot. This process is repeated recursively until all the elements are sorted
