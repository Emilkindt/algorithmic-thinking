### Growth of functions

- 随着 `n` 的增长, 如果 `f(n) : g(n)` 的比值始终趋于一个固定的常量, 则它们的增长速率相似.
- 随着 `n` 的增长, 如果 `f(n) : g(n)` 的比值趋于 `0`, 则 `f(n)` 增长的速度低于 `g(n)`.
- 随着 `n` 的增长, 如果 `f(n) : g(n)` 的比值趋于 `+∞`, 则 `f(n)` 的增长速率高于 `g(n)`.

### Techniques for comparing growth rates

- 在 graph 中, 如果有相同的 degree, 则两个多项式函数 `f(n)` 和 `g(n)` 则会以相同的速率增长, 且 lower degree 对它们的 "relative growth rate" 没有影响.
- 如果多项式函数 `f(n)` 的 degree 大于 `g(n)`, 则 `f(n)` 增长的会更快, 反之同理.
- 如果 `log(n)` 的增长速度大于常量 `1`, 且小于它的直线函数 `n`, 则 `nlog(n)` 的增长速度在 `n` ~ `n^2` 之间.
- 对任意指数函数 `a^n`, 当 `a > 1` 时该函数的增长速率大于任意多项式函数; 对任意阶乘函数 `n!` 其增长速率大于 `a^n`; 
