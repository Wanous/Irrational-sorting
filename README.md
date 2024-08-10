# [π] Irrational-sorting 
<div align="center"><img alt="banniere" align="center"  height="50%" width="100%" src="photos/TPI_banner.png"></div>

<div align=center>
  <img alt="Taille du code GitHub" src="https://img.shields.io/github/languages/code-size/Wanous/Irrational-sorting?label=taille%20du%20code">
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Wanous/Irrational-sorting?logo=github&style=plastic">
  <img alt="License" src="https://img.shields.io/github/license/Wanous/Irrational-sorting?style=plastic">
</div>

## Introduction
&nbsp;&nbsp;&nbsp;&nbsp;The Irrational sorting algorithm is an innovative method that uses irrational numbers to organize data. Specifically, it leverages the unique properties of these numbers to exchange and reorganize the data of a list until it's sorted. the idea is perhaps weird or even stupid
but it is **mathematically proven** that it works and that it can be considered as a sorting algorithm because it respects the fundamental laws of sorting algorithms, namely **correction** and **finiteness**.

## How it works ?
&nbsp;&nbsp;&nbsp;&nbsp;The sorting algorithm sort the items by repeatedly swapping their positions based on the digits of the irrational number used. For example, if the first two digits of the irrational number are 1 and 2, it would swap the first and second items in the list processed. The process continue, using more digits as needed, depending on the size of the list until the list is sort.

<div align="center"><img alt="banniere" align="center"  height="50%" width="50%" src="photos/Example_exchange.png"></div>

<div align="center"><h3>π : 3.1415...<mark><b>03</b></mark></h3></div>

> [!NOTE]  
>If the decimal points to an index that does not exist. For example the decimal points to index 9 in a list of 6 elements. The exchange is not performed.

## Handling Larger Lists
&nbsp;&nbsp;&nbsp;&nbsp;The algorithm adapts to different list sizes by using more digits from the irrational number as the list grows. For a list of 10 items, you use one digit at a time; for a list of 100 items, you use two digits at a time, and so on. This ensures that every item in the list can be properly sorted, even as the list size increases.

I calculate that with this equation : p = ⌈log<sub>10</sub>(n)⌉
- p ∈ ℕ*  : the interval of decimals to take 
- n ∈ ℕ*  : number of elements on the list
  
### Examples :
p = 1 : 1,4,1,5,9,2,6,5,3,5,8,9,7,... ← ‘141592653589793238462643383279…’  
p = 2 : 14,15,92,65,35,89,79,32,38,... ← ‘141592653589793238462643383279…’ 

(here it is the first decimals of π which are used for the example)

## Demonstration to prove the **correction** and **finiteness**
&nbsp;&nbsp;&nbsp;&nbsp;Proving both correction and finiteness is essential for establishing the reliability and practicality of the irrational sorting algorithm. Without these proofs, there would be no way to ensure that the algorithm could be used effectively in any situation. By carefully leveraging the properties of irrational numbers and probability theory, I successfully demonstrated that my algorithm will always sort a list correctly and will always finish the task in a finite amount of time.

<h3><mark>Correction</mark></h3>

> [!NOTE]  
> correction in the context of a sorting algorithm means that the algorithm will always produce a sorted list as output, regardless of the initial order of the elements. This property ensures that the algorithm is reliable and can be trusted to perform the sorting task accurately.

The algorithm makes swaps between items based on the digits of the irrational number. He can do it theoretically infinitely. Plus the algorithm is made in a while loop that will stop if the list is sorted. 
```
while is_sorted(my_list) == False :
    swap element in the list based on the digits
```
So if I prove that the list can be sorted then I can prove the correction, I already said that But proving that is by proving the Finiteness because the Finiteness is by sorting the list. *Understand ?*
It means that if I prove the Finiteness I prove the correction. It's the same with the bogo sort.

<h3><mark>Finiteness</mark></h3>

> [!NOTE]  
> Finiteness refers to the algorithm's ability to complete the sorting process in a finite amount of time. In other words, the algorithm should not run indefinitely; it should eventually stop once the list is sorted.

1. #### Valid Swaps: 
- The probability that the one indices randomly drawn in the interval $[0,10^p−1]$ for the swap are in the valid interval $[0,𝑛 − 1]$ is :
  $${n \over 10^p}$$
  But for a swap we need not one but two indices randomly drawn in the interval $[0,10^p−1]$ that are in the valid interval $[0,𝑛 − 1]$. So the correct probability is :
  $${n \over 10^p}\cdot{n \over 10^p}$$ so $${n^2 \over 10^{2p}}$$


**Example to understand** : If I take a list of 11 elements then n = 11 and I have an interval of 2 because p = ⌈log<sub>10</sub>(11)⌉ <=> 2, so the possible values ​​go from 0 to 99, 
This lead to 
$${11 \over 100}$$​ 
of having a valid index. And this is also equal to 
$${11 \over 10^2}$$​ 
that can be write 
$${n \over 10^p}$$​ 
With what I have said before

2. #### Well-sorted Swaps: 
- Each valid swap has a probability of 
$${1 \over 2}$$​ 
 of producing a well-ordered pair. 
 To determine this I done 
 
3. #### Combined Probability: 
- The combined probability that a valid swap produces a well-ordered pair is 
$${n \over 10^p}\cdot{1 \over 2}$$ so $${n^2 \over 2\cdot10^{2p}}$$

> [!IMPORTANT]
> **Conclusion :** Although the probability of each individual swap bringing the list to a completely sorted state is small, it is not zero. With enough swaps, the cumulative probability of getting a sorted list tends to 1. The non-zero probability of improvement at each swap ensures that the algorithm will not run forever without ever producing a complete order.
> This means that, theoretically, the algorithm will eventually sort the list completely, even though it may take a very large number of swaps.
> Therefore **finiteness** is prouved and so the **correctness** as well.


| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |
