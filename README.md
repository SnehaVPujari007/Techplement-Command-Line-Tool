<h1>Contacts CLI Tool</h1>
<h2>Overview</h2>
<p>The Contacts CLI Tool is a command-line application designed to manage and access your contacts easily. This tool allows you to add, update, delete, and search for contacts efficiently from the terminal.</p>

<h2>Table of Contents</h2>
<ol>
 <li>Installation</li> 
<li>Usage</li>
<li>Commands</li>
<li>Examples</li>
<li>Contributing</li>
</ol>

<h2>Installation</h2>
<b>Prerequisites</b></br>
<ul>Ensure you have Python 3.7 or above installed.</ul>
<ul>Installation Steps : </ul>

  <li>Clone the repository:</li>

<ul>git clone https://github.com/SnehaVPujari007/Techplement-Command-Line-Tool.git</ul>
<li>Navigate to the project directory:</li>

<ul>cd contacts-cli-tool</ul>
<li>Install the required dependencies:</li>

<ul>pip install -r requirements.txt</ul>
<li>Install the tool:</li>

<ul>python setup.py install</ul>
</ol>

<h2>Usage</h2>
<ul>After installation, you can use the contacts command to interact with your contacts list.</ul>

<li><b>Basic Command Structure</b></li>


<li><b>Commands</b></li></br>
<ol type = "1">
<li>Add a Contact</li> </br>
<ul>Add a new contact to your list : </ul>
<ul>contacts add --name "John Doe" --phone "123-456-7890" --email "john.doe@example.com"</ul> </br>
<li>Update a Contact</li> </br>
<ul>Update an existing contact's information : </ul>
<ul>contacts update --id 1 --name "John Smith" --phone "987-654-3210"</ul> </br>
<li>Delete a Contact</li> </br>
<ul>Delete a contact from your list : </ul>
<ul>contacts delete --id 1</ul> </br>
<li>Search for a Contact</li> </br>
<ul>Search for a contact by name or phone number : </ul>


<ul>contacts search --name "John"</ul> </br>
<li>List All Contacts</li> </br>
<ul>List all contacts in your address book : </ul>
<ul>contacts list</ul> </br>
</ol>
<h2>Examples</h2>
<li><b>Add a Contact</b></li> </br>

<p>contacts add --name "Alice Johnson" --phone "555-1234" --email "alice.j@example.com"</p>
<li><b>Update a Contact</b></li> </br>

<ul>contacts update --id 2 --phone "555-5678"</ul>
<li><b>Delete a Contact</b></li> </br>

<ul>contacts delete --id 3</ul>
<li><b>Search for a Contact</b></li> </br>

<ul>contacts search --name "Alice"</ul>
<li><b>List All Contacts</b></li> </br>

<ul>contacts list</ul>
<h2>Contributing</h2>
<li>Please follow these steps:</li> </br>
<ol type = "1">
<li>Fork the repository.</li>
<li>Create a new branch (git checkout -b feature-branch).</li>
<li>Commit your changes (git commit -m 'Add new feature').</li>
<li>Push to the branch (git push origin feature-branch).</li>
<li>Open a Pull Request.</li>
</ol> </br>


**By following this README, you should be able to set up, run, and understand the Contacts CLI Tool. Enjoy managing your contacts efficiently!😊**






