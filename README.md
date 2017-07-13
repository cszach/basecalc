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
            <td>Get help on a command. One <br/> argument is required, which is <br/> the command itself. i.e. ***? dec***
            </td>
        </tr>
        <tr>
        	<td>dec</td>
            <td>Convert a given number with its <br/> given base to decimal. Two <br/> arguments needed: the first one <br/> is the number, the second one is <br/> the base of that number. <br/> Example: ***dec 101010 2*** prints <br/> out ==*42*==</td>
        </tr>
        <tr>
        	<td>bin</td>
            <td>Convert a given number with its <br/> given base to binary. Two <br/> arguments are required: the first <br/> argument is the number, the <br/> second argument is the base of <br/> that number. <br/> Example: ***bin 64 16*** prints out <br/> ==*1100100*==</td>
        </tr>
        <tr>
        	<td>oct</td>
            <td>Convert a given number with its <br/> given base to octal. Two <br/> arguments are required: the first <br/> argument is the number, the <br/> second argument is the base of <br/> that number. <br/> Example: ***oct 895589 12*** prints out <br/> ==*10256771*==</td>
        </tr>
        <tr>
        	<td>hex</td>
            <td>Convert a given number with its <br/> given base to hexadecimal. Two <br/> arguments are required: the first <br/> argument is the number, the <br/> second argument is the base of <br/> that number. <br/> Example: ***hex 596 10*** prints out <br/> ==*254*==</td>
        </tr>
        <tr>
        	<td>input</td>
            <td>Save in a given number with its <br/> given base for later conversions <br/> Two arguments are required: the <br/> number and its base. <br/> Example: ***input 90 11***</td>
        </tr>
        <tr>
        	<td>-></td>
            <td>Convert the saved number to either <br/> binary, decimal, octal, or <br/> hexadecimal. An argument is <br/> required: the base you want to <br/> convert to. Either *bin*, *dec*, *oct* or *hex* <br/> For instance, if the user previously <br/> input *input 65 10*, the output of ***-> hex*** <br/> should be ==*41*==. The outut of ***-> bin*** <br/> should be ==*1000001*==</td>
        </tr>
        <tr>
        	<td>exit</td>
            <td>Exit the calculator</td>
        </tr>
    </tbody>
</table>
- - -
## Error Reports
Please send error reports to novakglow@gmail.com
- - -
## License
Apache-2.0
