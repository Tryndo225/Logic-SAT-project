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

## Documentation
This script is resposible for encoding an graph input into a [Conjuctive normal form (CNF)](https://en.wikipedia.org/wiki/Conjunctive_normal_form) for [Hamiltonian path](https://en.wikipedia.org/wiki/Hamiltonian_path) detection. <br>
It has both a User interface input method and a **Input Field** input method. For further information look at [Action Fields](#action-fields) and [Step-by-step walkthrough](#step-by-step-walkthrough).

## Example inputs
1. Complete Graph on 3 vetexes: `(1,3);(3,2);(2,1);(1,2);(2,3);(3,1)` ![Complete Graph on 3 (example 1)](/assets/images/san-juan-mountains.jpg "San Juan Mountains") Any path of 3 vertex is a valid hamiltonian path. Path through `2, 1, 3` found.
2. Second item
3. Third item
4. Fourth item 
