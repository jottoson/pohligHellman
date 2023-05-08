# pohligHellman
An implementation of the Pohlig-Hellman Algorithm for MATH 523 at Cal State University, San Marcos in Spring 2023. Copy and paste the code into CoCalc to try it out!

The paper follows closely the work "An Introduction to Mathematical Cryptography" by Hoffstein, Pipher, and Silverman.The program implements the version of Pohlig-Hellman given in Theorem 3.3 of the included paper in order to solve the Discrete Logarithm Problem (DLP) g^x = h mod p. 

Note that I used the sympy library in order to generate the prime factorization of p-1. I included a function that I made to generate the prime factorization, but it runs very slowly. Sympy is included in CoCalc, so the program should work as-is.

Below are the public keys from the second codebreaking competition in class, along with the solution and corresponding plaintext. Try using the included program to watch all of our encrypted messages crumble before the power of Pohlig-Hellman. The messages were encrypted using the Elgamal Public Key Cryptosystem. If you are not familiar, then a short description is included at the bottom for reference.



Group #1 - Optimus Prime Minus One
Public Key (p,g,A) = (9436835835813811,9436835835813593,7299905945240414)

Private Key a = 9386432517586548

Encrypted Messages (c1, c2)
(4945742015458503,6103709962158699)
(1423113634697436,8412668216133305)
(5326870832475772,5652089253467885)
(3860200279819464,942949475674878)

Plaintext
TO BE OR NOT TO BE THAT IS THE QUESTION

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

Group #2 - Encryptors
Public Key (p,g,A) = (88888888888889,3,74155098271818)

Private Key a = 619

Encrypted Messages (c1, c2)
(59049,87421365191081)
(59049,27010923969375)
(59049,85430579971057)
(59049,70436724738666)
(59049,2016495773694)
(59049,34826023630825)
(59049,59983732059526)
(59049,17845376118235)
(59049,70413747354125)

Plaintext
THE BIG BANG THEORY IS A GREAT TV SHOW DID YOU CRACK OUR CODE YET BAZINGA

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

Group #3 - KryptoCa$h23
Public Key (p,g,A) = (9999999999999851, 7238097565952926, 5186693351008771)

Private Key a = 6839099439816327

Encrypted Messages (c1, c2)
(5675392474169380, 5903602515298855)
(6088725960081302, 3616758893379575)
(8060150755502508, 2936453241174499)
(7710513992822768, 6278345956458697)
(26216713918793, 379501012175768)
(6998268462137408, 2884364685945528)
(5806152646791670, 8949339045111255)
(8738478660874093, 7684156021018518)

Plaintext
SINGAPORE FERTILITY RATE HITS NEW LOW PUTTING FOCUS ON HOUSING PRICES

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

Group #4 - Lingering Lizards
Public Key (p, g, A) = (34127252370851, 109, 32245248204905)

Private Key a = 964067211

Encrypted Messages (c1, c2)
(10467823339758,20266423863386)
(30234991241062,33686536742262)
(26019556828232,29412247488664)
(22685496003723,29428100673725)
(1593602230576,24338130119180)
(20909955291220,18210063512303)
(30346993864996,7356749552861)
(8408928774280,5310542437368)
(20448848756110,19227724670686)
(26364072013836,6675298325018)
(4859626727485,14126078237765)
(28604188688752,10066041394408)
(18941313302168,9627953521525)
(1892307672134,16372393121)

Plaintext
YOUR NEW BELOVED GERMAN SHEPHERD AFGHAN HOUND CHOW CHOW MIX HAS BROUGHT US JOY DURING A VERY DIFFICULT TIME

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

Group #5 - Maine Coons
Public Key (p, g, A) = (76363692347,56891593216,40336523883)

Private Key a = 39274501710

Encrypted Messages (c1, c2)
(23128352208,60455154486)
(23128352208,14569167002)
(23128352208,245683111)
(23128352208,15038319607)
(23128352208,16516415992)
(23128352208,51555670205)
(23128352208,42916463425)
(23128352208,67976051227)

Plaintext
YOU CAN BECOME ANYTHING IF I PUT MY MIND TO IT XXXX

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

Version of Elgamal Public Key Cryptosystem used for this competition:
Alice chooses a prime p and a primitive root g mod p. Alice then chooses a secret number a to act as her private key and computes A = g^a mod p. Alice publishes her public key (p, g, A).

Bob wants to send a message to Alice. He first chooses a random number k modulo p, which exists solely to encrypt a single message. Bob takes his plaintext message m, converts it to upper case, and write down the ASCII code for each character. For example, if m = "Hello", then Bob would write down 7269767679, since the ASCII code for "H" is 72, the ASCII code for "E" is 69, and so on. Bob then splits up this number into chunks of equal size, where each chunk must be smaller than p. He then computes two quantities for each chunk: c1 = g^k mod p; and c2 = m * A^k mod p. Each chunk becomes (c1, c2). Bob repeats this process for each chunk of his message, and when he is finished he sends all of the (c1, c2) ordered pairs to Alice.

Alice receives the encrypted messages as ordered pairs of the form (c1,c2). For each chunk, she computes x = (c_1^a)^-1 mod p. That is, she computes the inverse modulo p of (c_1)^a. She then computes m = x * c_2 mod p. This m value will be the chunk of Bob's message as ASCII values, which she can then write as English characters.
