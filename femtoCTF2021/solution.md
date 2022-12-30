# Phase 1 - Login:
When pressing on signin we are sent to look at the source code inorder to find 
the password, which is hardcoded into 'secret.go' file.  
password is: `planet!!!11`

It seems like there is no place to insert the password but by playing 
around with the inspect tool we can see that there is a transparent input
element above the signin button.

# Phase 2 - Known plaintext attack:
By looking at the site trafic we can see that
when sending the currect password we get two tokens back,**USER** and **TEST**.
A quick review of the code shows that there is a page named 'debug'
that checks the "TEST" token and extracts an IP out of it.
In the case that the IP is localhost (127.0.0.1) the request
redirects to another page named 'admin'.

Ok, so it seems that we need to manipulate the token in such a way that
it will look like the IP is localhost.

We have the source code so we can see how the token is made.

The tokens are encrypted with AES128-CBC.
The key is random and generated in a safe way so we can't decyrpt
the token, but we do know the plaintext and because the token algorithm
uses AES-CBC we can change the encrypted data to be anything we want by using 
a known plaintext attack on the ciphertext.

## This is how it works:

The ciphertext is **Encrypt(IV (+) plaintext)**
and the decryption process is decrypt and then xor with the IV.
The IV is passed as the first half of the token, so we know it and can change it.  

lets change it to **IV (+) plaintext (+) our_new_msg**.  
That way xoring the decrpted msg will yield our new msg.

# Phase 3 - BoF:
After passing the localhost barrier we can get 
to the 'admin' page.
This page gets a GET request with two parameters, **input** and **dbg**.
The parameters are passed to a function named **get_flag**
which implemented in a dynamic library.

Now, we can solve this into two different ways.

The first is by looking at the assebly code with disassembler.
The second is by fuzzing the input parameter.

### The dissasembler way:
Using a disassembler we can look at the assembly instructions of 
the function and we can see that the length of the input parameter is not limited as it supposed to be, 
and causing a BoF which allows us to change the code flow in a way that the program will call **flag()** instead of **not_a_flag()**.
From here all we got to do is to check the address of **flag** and see the value we need to overwrite.

### The Fuzzing way:
To my opinion this approach is more realistic, in a real scenario
we probably wouldn't have the source code or even the binary to disassemble.
since we have the **dbg** parameter we can print our input buffer back,
so we can start by entering a large input and see what's happends.
By doing so we see that we can overwrite between 1 to 2 bytes of the the flag function address. 2 bytes is 2^16 different possibilities, that's doable.
So to solve this I wrote a fuzzer in Golang that checks all the possibilities
really fast and sends back the flag. To make it more challenging I limited it all to a single token which is valid only for 5 minutes.
Anyway by using enough threads you'll only need a few seconds..

And thats it. We got the flag!
