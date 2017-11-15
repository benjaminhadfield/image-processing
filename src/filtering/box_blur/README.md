# Box Blur

This is one of simplest low-pass filters. It simply convolves an image with an `n × n`
kernel of `1`s.

For example, a `3 × 3` kernel

```
1 ⎡ 1 1 1 ⎤
− ⎢ 1 1 1 ⎥
9 ⎣ 1 1 1 ⎦
```
