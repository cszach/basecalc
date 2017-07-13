# Base Calculator
- - -
## About
A calculator with CLI used to convert numbers in between base.
Written in Python
Kit: PyCharm
Latest version release: 1.0.0
- - -
## Instructions
The calculator itself is self-explanatory already
Here is the list of commands:
<table>
	<thead>
    	<tr>
        	<th colspan="2">Commands</th>
        <tr>
    </thead>
    <tbody>
    	<tr>
        	<td>help</td>
            <td>Show commands and their details</td>
        </tr>
        <tr>
        	<td>?</td>
            <td>Get help on a command. One <br/> argument is required, which is <br/> the command itself. i.e. <b><i>? dec</i></b>
            </td>
        </tr>
        <tr>
        	<td>dec</td>
            <td>Convert a given number with its <br/> given base to decimal. Two <br/> arguments needed: the first one <br/> is the number, the second one is <br/> the base of that number. <br/> Example: <b><i>dec 101010 2</i></b> prints <br/> out <i>42</i></td>
        </tr>
        <tr>
        	<td>bin</td>
            <td>Convert a given number with its <br/> given base to binary. Two <br/> arguments are required: the first <br/> argument is the number, the <br/> second argument is the base of <br/> that number. <br/> Example: <b><i>bin 64 16</i></b> prints out <br/> <i>1100100</i></td>
        </tr>
        <tr>
        	<td>oct</td>
            <td>Convert a given number with its <br/> given base to octal. Two <br/> arguments are required: the first <br/> argument is the number, the <br/> second argument is the base of <br/> that number. <br/> Example: <b><i>oct 895589 12</i></b> prints out <br/> <i>10256771</i></td>
        </tr>
        <tr>
        	<td>hex</td>
            <td>Convert a given number with its <br/> given base to hexadecimal. Two <br/> arguments are required: the first <br/> argument is the number, the <br/> second argument is the base of <br/> that number. <br/> Example: <b><i>hex 596 10</i></b> prints out <br/> <i>254</i></td>
        </tr>
        <tr>
        	<td>input</td>
            <td>Save in a given number with its <br/> given base for later conversions <br/> Two arguments are required: the <br/> number and its base. <br/> Example: <b><i>input 90 11</i></b></td>
        </tr>
        <tr>
        	<td>-></td>
            <td>Convert the saved number to either <br/> binary, decimal, octal, or <br/> hexadecimal. An argument is <br/> required: the base you want to <br/> convert to. Either <i>bin</i>, <i>dec</i>, <i>oct</i> or <i>hex</i> <br/> For instance, if the user previously <br/> input <i>input 65 10</i>, the output of <b><i>-> hex</i></b> <br/> should be <i>41</i>. The outut of <b><i>-> bin</i></b> <br/> should be <i>1000001</i></td>
        </tr>
        <tr>
        	<td>exit</td>
            <td>Exit the calculator</td>
        </tr>
    </tbody>
</table>
<hr/>
<h2>Error Reports</h2>
<span>Please send error reports to novakglow@gmail.com</span>
<hr/>
<h2>License</h2>
<span>Apache-2.0</span>