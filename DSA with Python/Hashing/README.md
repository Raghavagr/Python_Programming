## Hashing

It is a method of sorting and indexing data. The idea behind hashing is to allow large amount of data to be indexed using keys commonly created by formulas.

**Why Hashing**

- It is efficient in search operation

**Hashing Terminology**

1. **Hash Function** - function that can be used to map of arbitrary size of data to fixed size.
2. **Key** - Input data given by User.
3. **Hash Value** - Value returned by Hash function.
4. **Hash Table** - data structure which implements an associative array abstract data type, a structure that can map keys to values.
5. **collision** - It occurs when two different keys to a hash function produces the same output.

**Properties of Good Hash Function**

- It uniformly distributes hash values across hash Table which means no collision condition should occur
- It has to use all input data.

**Types of Collision Resolution Techniques**

1. **Direct Chaining** - It implements the buckets as a linked list. colliding elements are stored in this list.
2. **Open Addressing** - Colliding elements are stored in other vacant buckets. during storage and lookup these are found through so called probing. Now for probing we have two techniques.
  - **Linear Probing** - Places new key into closest following empty cell.
  - **Auadratic Probing** - Adding arbitrary quadratic polynomial to the index until an empty cell is found.
  - **Double Hashing** - Interval between probs is computed by another hash function.

**What Happend when Hash table is full**

The condition will never arise in Direct chaining.
Now when we use open addresing
