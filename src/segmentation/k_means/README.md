# K-Means

K-Means is an unsupervised method for assigning discrete labels to unstructured
data based on their proximity to the centroid of clusters.


## Algorithm

The type of the implemented algorithm is

```
kmeans :: [Num] -> Num -> ([Num], [Fractional])
```

The algorithm proceeds as follows:

 - For inputs `X : list of points`, `k : number of clusters`
 - Let `C` be `k` centroids, placed at random locations
 - Repeat until convergence:
    * For each point `xᵢ` ∈ `X`
        * Assign `xᵢ` to centroid `cⱼ` ∈ `C`, such that `cⱼ` is found using `argmin(j) Dist(xᵢ, cⱼ)`
    * For each centroid `cⱼ` ∈ `C`
        * Set `cⱼ` equal to the mean of all points assigned to `cⱼ`
