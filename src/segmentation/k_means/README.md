# K-Means

K-Means is an unsupervised method for assigning discrete labels to unstructured
data based on their proximity to the centroid of clusters.


## Algorithm

The type of the implemented algorithm is

```
kmeans :: [Num] -> Num -> ( [Num], [(Fractional, Fractional)] )
```

The algorithm proceeds as follows:

 - For inputs `X : list of points`, `k : number of clusters`
 - Let `C` be `k` centroids, placed at random locations
 - Repeat until convergence:
    * For each point `x<sub>i</sub>` ∈ `X`
        * Assign `xi` to the nearest centroid `c<sub>j</sub>`, where `c<sub>j</sub>` is found by `argmin(j) Dist(x<sub>i</sub>, c<sub>j</sub>)`
    * For each centroid `c<sub>j</sub>` ∈ `C`
        * Set `c<sub>j</sub>` equal to the mean of all points assigned to `c<sub>j</sub>`
