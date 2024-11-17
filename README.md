# Hamiltonian path SAT solver
> This is a solution for a homework from Propositional and Predicate Logic (NAIL062) and it is a python script that is resposible for encoding a set of vertexes and edges into a suitable formula for sat solver to find a hamiltonina path. It also calls the solver and interprets it's solution to human readable and understandable form.

## How to run
**!!!Important!!!** it needs [Glucose 4.2.1](https://github.com/audemard/glucose/releases/tag/4.2.1) to run and count's on it's proper instalation and the fact that is able to be run globaly and thus located in `/usr/local/bin/` folder.

### Step-by-step walkthrough
Upon running the script you are prompted to choose the amount of vertexes, this requires the user to input any number, however high numbers make the UI hectic and nearly impossible to work in thus forcing user to rely on the input text field and console as output. 
When the number of vertices is entered a UI using the python `tkinter` library is displayed. This is where most of the user interaction will happen. 
Use your mouse to select vertexes to connect with an edge (clicking on a vertex marks it with red fill and selecting another one will create an edge (if vertex is selected it can be clicked again to be unselected)). If the an edge is alredy present between vertexes selecting them again (in the same order) will delete the edge. 
Edges are directed thus for undirected uses user has to create one edge for one direction and another one for the backwards traversal. When the wanted input is entered user is to click one of the action buttons to perform actions.

### Action Fields
The **Solve** button: 
> sends the proble to [Glucose 4.2.1](https://github.com/audemard/glucose/releases/tag/4.2.1) to solve and takes you to a seperate window where (if any possible) a valid hamiltonian path is displayed in none exists a empty graph will be displayed.

The **Reset** button:
> resets the the whole program and makes the user start from begining (best used when different amount of edges is wanted, for clearing the the input it is better to just delete edges from the **Input Field** and clicking the **Parse** button).

The **Parse** button:
> as the name suggest this button is resposible for parsing the input from **Input Field**.

The **Input Field** area:
> here the user can manualy make changes to the edges of the graph. The input is simple, use `;` as a delimiter between edges and `,` as a delimiter between vertexes of an edge. For better readability `(`, `)`, and `<SpaceBar>` can be used, 
however these are competely ignored during parsing and surve just to mek the input more user friendly. Therefore caution with `;` and `,` and their proper use is advised. <br>
> **Example input:** On 5 vertexes: (1,2);(2,3);(3,4);(4,5) => reuslts in a output of hamiltonian path going through vertexes: 1, 2, 3, 4, 5

The **Results**/**Input** buttons:
> these serve as a means of traversing between results and input screen, beware that none of them make any change to the content of the pages thus for new result screen **Solve** button has to be pressed or the last result will remain displayed.

## Encoding
Encoding to [Conjuctive normal form (CNF)](https://en.wikipedia.org/wiki/Conjunctive_normal_form) is done in a way there every vertex has a set of variable where each one of them coresponds to a sigle position in path, meaning that grapth of $n$ vertices will have $n^2$ variables. This means that for a grapth of 3 vertices would have 9 variables that go as following ($(V_1)_2$ means vertex 1 is in position 2):
1. $(V_1)_1 = 1$
2. $(V_1)_2 = 2$
3. $(V_1)_3 = 3$
4. $(V_2)_1 = 4$
5. $(V_2)_2 = 5$
6. $(V_2)_3 = 6$
7. $(V_3)_1 = 7$
8. $(V_3)_2 = 8$
9. $(V_3)_3 = 9$

Then using this format of variables we crete the problem using a few simple statements makers:
### oneVertexAtPos
> This function ensures that each position in the path has at least one vertex. (For every pos n in the path $(V_1)_n$ or $(V_2)_n$ or $(V_3)_n$ or ... or $(V_n)_n$)
## everyVertexMaxOnce
> This function ensures that each vertex appears in path maximum once. (For v in vertexes, for n1, n2 in positions v isn't on n1 or isn't on n2)
### everyVertexVisited
> This function ensures that each vertex appears in the path at at least one position. (For every vertex v in the graph $(V_v)_1$ or $(V_v)_2$ or $(V_v)_3$ or ... or $(V_v)_n$)
### maxOneVertexAtEachPos
> This function ensures that each position in path cannot be occupied 2 vertices at once. (For n in positions, for v1, v2 in vertices: v1!=v2, v1 isn't on n or v2 isn't on n)
### pathConsistOfActualEdges
> This function ensures that the path consist only of valid edges inputed. (For v1, v2 from vartices, if (v1, v2) not in edges: for every position n v1 not on pos n or v2 not on pos n+1)

This leaves us with a functional [Conjuctive normal form (CNF)](https://en.wikipedia.org/wiki/Conjunctive_normal_form) equation, we can just send to [Glucose 4.2.1](https://github.com/audemard/glucose/releases/tag/4.2.1).


## Documentation
This script is resposible for encoding an graph input into a [Conjuctive normal form (CNF)](https://en.wikipedia.org/wiki/Conjunctive_normal_form) for [Hamiltonian path](https://en.wikipedia.org/wiki/Hamiltonian_path) detection. <br>
It has both a User interface input method and a **Input Field** input method. For further information look at [Action Fields](#action-fields) and [Step-by-step walkthrough](#step-by-step-walkthrough).

## Example inputs
1. Complete graph on 3 veteces: `(1,3);(3,2);(2,1);(1,2);(2,3);(3,1)` ![Complete Graph on 3 (example 1)](/assets/images/completeOn3.png "Complete graph on 3")<br> Any path of 3 unique vertex is a valid hamiltonian path.<br> Found a result: `Hamiltonian path goes as through vertexes as follows: 2, 1, 3` ![Complete Graph on 3 result(example 1)](/assets/images/completeOn3Result.png "Complete Graph on 3 Result")<br>
2. Non-Hamiltonian graph on 5 vertices: `(2,1);(1,3);(4,5);(4,3);(1,5);(3,5);(4,1)` ![Non-Hamiltonian graph on 5 (example 2)](/assets/images/non-hamiltonianOn5.png "Non-hamiltonian graph on 5") <br> No path found. <br> ![Non-Hamiltonian graph on 5 result(example 2)](/assets/images/non-hamiltonianOn5Result.png "Non-hamiltonian graph on 5 result")<br>
3. Hamiltonian grapth on 100 vertices:`(97,88);(23,86);(45,36);(35,12);(48,56);(30,14);(56,17);(61,73);(28,19);(77,3);(100,60);(33,52);(14,62);(7,8);(9,4);(4,64);(93,82);(32,79);(72,81);(37,89);(47,76);(73,23);(95,16);(96,94);(90,69);(57,25);(60,9);(58,78);(56,4);(64,13);(60,11);(6,20);(75,11);(53,74);(57,15);(66,90);(25,96);(78,44);(32,24);(20,5);(52,37);(27,2);(79,87);(29,38);(87,75);(94,18);(46,45);(63,6);(50,68);(38,67);(55,85);(85,80);(17,73);(51,77);(44,94);(36,84);(65,35);(91,26);(44,40);(24,48);(70,61);(62,66);(81,47);(98,57);(3,33);(43,71);(34,46);(99,65);(16,29);(80,22);(84,97);(8,15);(10,21);(4,39);(1,51);(67,72);(86,30);(49,53);(22,64);(71,79);(11,31);(13,27);(93,49);(76,98);(88,91);(19,43);(82,42);(31,95);(39,63);(40,100);(2,99);(92,70);(36,32);(17,54);(54,92);(41,49);(21,84);(74,34);(26,50);(18,58);(5,93);(42,1);(83,55);(83,31);(89,83);(59,41);(68,7);(69,28);(12,10)` ![Hamiltonian graph on 100 (example 3)](/assets/images/hamiltonianOn100.png "Hamiltonian graph on 100") <br> Fount a result: `Hamiltonian path goes as through vertexes as follows: 59 41 49 53 74 34 46 45 36 32 24 48 56 17 54 92 70 61 73 23 86 30 14 62 66 90 69 28 19 43 71 79 87 75 11 31 95 16 29 38 67 72 81 47 76 98 57 25 96 94 18 58 78 44 40 100 60 9 4 39 63 6 20 5 93 82 42 1 51 77 3 33 52 37 89 83 55 85 80 22 64 13 27 2 99 65 35 12 10 21 84 97 88 91 26 50 68 7 8 15` <br> ![Hamiltonian graph on 100 result(example 3)](/assets/images/hamiltonianOn100Result.png "Hamiltonian graph on 100 result")
