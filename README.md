# Quantum Physics & Quantum Computation
本项目收集了量子物理、量子计算相关书籍和文章。

## 入门篇

* [Griffiths - Introduction to quantum mechanics](https://github.com/XinjianOUYANG/Quantum_Physics/blob/7cb19c0f4a429169b923b7f4d76bf49765b10b28/%E9%87%8F%E5%AD%90%E5%8A%9B%E5%AD%A6/Griffiths%20-%20Introduction%20to%20quantum%20mechanics.pdf)

* [量子力学讲义](https://github.com/XinjianOUYANG/Quantum_Physics/blob/dd1ef7c9bce9ce2767fd79484a0f9c0e9c0838cf/%E9%87%8F%E5%AD%90%E5%8A%9B%E5%AD%A6%20-%20%E6%B8%85%E5%8D%8E%E7%89%A9%E7%90%86%E7%B3%BB/0%20-%20%E7%9B%AE%E5%BD%95.pdf) 清华大学

* [Quantum Computation and Quantum Information](https://github.com/XinjianOUYANG/Quantum_Physics/blob/e3b40ca3218374727359e180b3472d21b879fc96/%E9%87%8F%E5%AD%90%E8%AE%A1%E7%AE%97&%E9%87%8F%E5%AD%90%E9%80%9A%E4%BF%A1/Quantum%20Computation%20and%20Quantum%20Information.pdf) Michael A. Nielsen & Isaac L. Chuang
10th Anniversary Edition

内容提要：
     
     本书完整系统地介绍了量子计算与量子信息的研究成果和基本知识，主要内容包括基本概念、量子路、量子Fourier 变换及其应用、量子搜索算法和量子计算机的物理实现

* Berkeley edX course CS191x [Quantum Mechanics and Quantum Computation](https://www.youtube.com/playlist?list=PLDAjb_zu5aoFazE31_8yT0OfzsTcmvAVg) video lecture series by Professor Umesh Vazirani. 

*  [Quantum Computer Science: An Introduction](https://github.com/XinjianOUYANG/Quantum_Physics/blob/e3b40ca3218374727359e180b3472d21b879fc96/Quantum%20Computer%20Science_An%20Introduction.pdf) N. David Mermin Cornell University

主要内容：

     Lecture 1 - Double-slit experiment
   
     Lecture 2 - Qubits and uncertainty principle

     Lecture 3 - Axioms of QM, two qubits, and entanglement

     Lecture 4 - Bell Inequalities

     Lecture 5 - Quantum gates

     Lecture 6 - Quantum teleportation

     Lecture 7 - Quantum circuits

     Lecture 8 - Early quantum algorithms

## 进阶篇

* [Shankar - Principles of quantum mechanics](https://github.com/XinjianOUYANG/Quantum_Physics/blob/8254bbc11483e7dedede9ef3e92af905475d8342/%E9%87%8F%E5%AD%90%E5%8A%9B%E5%AD%A6/Shankar%20-%20Principles%20of%20quantum%20mechanics.pdf)

* [The Theory of Quantum Information](https://github.com/XinjianOUYANG/Quantum_Physics/blob/8254bbc11483e7dedede9ef3e92af905475d8342/%E9%87%8F%E5%AD%90%E8%AE%A1%E7%AE%97&%E9%87%8F%E5%AD%90%E9%80%9A%E4%BF%A1/The%20Theory%20of%20Quantum%20Information%20John%20Watrous%20Institute%20for%20Quantum%20Computing%20University%20of%20Waterloo.pdf) John Watrous, Institute for Quantum Computing, University of Waterloo. 课程[讲义](https://cs.uwaterloo.ca/~watrous/TQI/)

* [QUANTUM COMPUTING From Linear Algebra to Physical Realizations](https://github.com/XinjianOUYANG/Quantum_Physics/blob/8254bbc11483e7dedede9ef3e92af905475d8342/%E9%87%8F%E5%AD%90%E8%AE%A1%E7%AE%97&%E9%87%8F%E5%AD%90%E9%80%9A%E4%BF%A1/QUANTUM_COMPUTING_From_Linear_Algebra_to.pdf) Mikio Nakahara, Department of Physics, Kinki University, Higashi-Osaka, Japan

* Quantum Optics(量子光学)
     [quantum optics: An introduction](https://github.com/XinjianOUYANG/Quantum_Physics/blob/dd1ef7c9bce9ce2767fd79484a0f9c0e9c0838cf/%E9%87%8F%E5%AD%90%E5%85%89%E5%AD%A6/Fox%20M.%20Quantum%20optics..%20an%20introduction%20(Oxford,%202006)(ISBN%200198566735)(397s)_PQ) Mark Fox
    
### 经典文章

（1）Grover 算法的推广，离散量子游走算法：

* Watrous, J. Quantum simulations of classical random walks and undirected graph connectivity. in Proceedings. Fourteenth Annual IEEE Conference on Computational Complexity (Formerly: Structure in Complexity Theory Conference) (Cat.No.99CB36317) 391, 180–187 (IEEE Comput. Soc, 1999).

（2）量子傅里叶变换即其推广(Shor 算法)：

* Childs, A. M. & van Dam, W. Quantum algorithms for algebraic problems. Rev. Mod. Phys. 82, 1–52 (2010).5
将问题转换成Spatial Search问题的一般思路，这个读起来难一点：

* Ambainis, A. Quantum Walk Algorithm for Element Distinctness. in 45th Annual IEEE Symposium on Foundations of Computer Science 37, 22–31 (IEEE, 2003).

## 数学基础

* 群论[Group Theory in a Nutshell for Physicists]()
* [Mathematical Methods for Physics and Engineering](), 参考书，随用随学

### 一些建议

1. 硬件层面，量子光学是比较基础好学的，推荐scully Zubairy ，quantum optics 前半本书，有时候得算effective Hamiltonian 甚至重整化群，还得补补数学，群论，QFT，但是可以要用再学。然后就是最好把学到的量子光学技术应用于一个具体的设备，cavityQED，nmr或者circuitQED，自己谷歌一些综述推一下。
硬件软件结合层。这也是多数理论工作者在的地方，例如量子控制，量子模拟，特殊系统的量子算法，这要看自己的方向了。
2. 软件层。preskill 的Quantum Information 讲义，习题非常有意思，可以在研究生入学之后和师兄弟，老师好好一起讨论，如果条件允许。Nielsen&Chuang的书是经典教材。
3. PS，量子计算与信息对数学物理素养有一定要求，应该多多研读。

### 参考
* 知乎文章[量子计算与量子信息的一些材料](https://zhuanlan.zhihu.com/p/34183937)
* 
