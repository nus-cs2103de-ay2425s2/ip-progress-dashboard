%%[This page was last updated on Nov 30 2024]%% [**<span class="text-warning">:octicon-eye:</span> indicates those _watching_ the forum** (kudos :+1:)]


<panel type="info"  collapsed>
<div slot="header">

### 1. DONO.. JIE `@xenthm` (16 posts) 
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/41" expanded>
<div slot="header">

**1. :fas-info-circle: How do we represent inheritance from a generic class?**
</div>

# Question
In my team's project, the classes `AuthorList` and `MangaList` both inherit from the generic `ArrayList`. The exact code used is of the format: 
```
public class AuthorList extends ArrayList<Author> ``{``
    ...
``}``
```
Is the method of representing this inheritance structure depicted in the referenced picture valid? If not, how else can we represent it? 

# Reference
>![Screenshot 2024-10-30 132426](https://github.com/user-attachments/assets/991bbc44-a203-415b-8f97-c46f2f15afc5)
In this diagram, MangaList and AuthorList are indicated as inheriting from ArrayList, but with notes stating "ArrayList<Manga>" and "ArrayList<Author>". I think that, unless these two classes inherit from ArrayList<T> (in which I think you should remove the notes), I believe that there is no inheritance to indicate?

_Originally posted in a comment in https://github.com/nus-cs2113-AY2425S1/tp/pull/9#discussion_r1821904048_
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/33" expanded>
<div slot="header">

**2. :fas-info-circle: Questions regarding UML diagrams**
</div>

# 1. Do UML Object Diagrams require that their associations show navigability from the corresponding class diagram?
Referring to the 2nd question in L8-Exercises, the object diagram from the answer that corresponds to the class diagram mirrors the navigability of the association between `Book`, and `ISBN` and `CallNumber`. However, I couldn't find any mention of this from the notes over at [`Object Diagrams → Associations`](https://nus-cs2113-ay2425s1.github.io/website/se-book-adapted/chapters/uml.html#associations-2). 
>Class Diagram from L8-Exercises ![image](https://github.com/user-attachments/assets/7ce74b01-e3e8-49aa-a895-6279cba52b49)
>Object Diagram answer from Canvas video ![image](https://github.com/user-attachments/assets/afde91e5-0f3f-402a-8b69-268c43baa327)
# 2. Does the existence of multiplicity imply navigability?
Referring to the 2nd question in L8-Exercises, the association class `Loan` has the multiplicity `1` indicated on both ends of the dashed line that connects to the association link between `Book` and `Student`. How do we know that `Loan` has references to &lt;ins>both&lt;/ins> `Book` and `Student` (aside from reasoning with the desired associations with common sense)?
>Class Diagram from L8-Exercises ![image](https://github.com/user-attachments/assets/fbdf10ec-4d4e-493a-a2e2-b278a2851030)
>Object Diagram answer from Canvas video ![image](https://github.com/user-attachments/assets/a56a38c9-5a7a-4e52-b4fe-3c2f81a5562a)
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/25" expanded>
<div slot="header">

**3. :fas-info-circle: Rebasing when syncing personal forks for tP**
</div>

[Appendix E: Using GitHub](https://nus-cs2113-ay2425s1.github.io/website/admin/appendixE-gitHub.html#d-using-prs-to-track-task-progress) instructs us to avoid rebasing when when merging PRs. 

Can we do that when managing our own fork instead? The goal is to keep our fork commit history cleaner. 
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/11" expanded>
<div slot="header">

**4. :fas-info-circle: Wrong Constraint-Java-Version on tP Constraints website**
</div>

The required Java version indicated over at [https://nus-cs2113-ay2425s1.github.io/website/admin/tp-constraints.html#constraint-java-version](https://nus-cs2113-ay2425s1.github.io/website/admin/tp-constraints.html#constraint-java-version) is incorrectly stated as Java 11. Is this the case or should it be Java 17 as mentioned in Week 1?

![image](https://github.com/user-attachments/assets/637c22b4-04ba-41ff-ba4a-c4f8fcbebbe4)

</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/3" expanded>
<div slot="header">

**5. :fas-info-circle: Excessive emails from Archipelago**
</div>


Archipelago sends excessive Session Invitation emails with an invite link to the Lecture Session. Refer to the screenshot below. 

![image](https://github.com/user-attachments/assets/85a79af1-c9aa-4ca0-876d-82158d663dc0)


</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/3#issuecomment-2313092649" expanded>
<div slot="header">

**6 :fas-comment:**
</div>

Thank you Prof! Will monitor on Friday before the lecture. 
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/3#issuecomment-2320912292" expanded>
<div slot="header">

**7 :fas-comment:**
</div>

I received only 3 emails this time. Big improvement from last week haha. I will close the issue now!
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/11#issuecomment-2329569149" expanded>
<div slot="header">

**8 :fas-comment:**
</div>

Hi Prof, it still says "version 11" on the site. 
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/25#issuecomment-2395933511" expanded>
<div slot="header">

**9 :fas-comment:**
</div>

> Would it not affect the branches you create further and create PRs from?

Yes, my understanding is that it will reduce the clutter on my fork as a result of merge commits from other PRs from upstream. 

That being said, I think that that will cause issues when I create my own PRs since my fork's commit history will be different from the upstream's. 
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/25#issuecomment-2395967731" expanded>
<div slot="header">

**10 :fas-comment:**
</div>

Alright, I will stick with merging then. 

> avoid rebasing when when merging PRs

As for this, am I right to say that the motivation is to ensure that the automated checks for tP progress work as intended?
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/25#issuecomment-2396026821" expanded>
<div slot="header">

**11 :fas-comment:**
</div>

Thank you Prof!
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/24#issuecomment-2406399560" expanded>
<div slot="header">

**12 :fas-comment:**
</div>

Hi Prof, will we be penalised if we make these classes utility classes (only static methods without instantiating as mentioned). I just came across this issue today. 
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/33#issuecomment-2408953315" expanded>
<div slot="header">

**13 :fas-comment:**
</div>

Noted for Q1, thank you! As for Q2, I saw the video and noted that `Loan` has references to both `Book` and `Student`. To clarify my question, is it safe to assume that as long as we have an association class like `Loan`, it means we should represent it in the way in the video?
![image](https://github.com/user-attachments/assets/e8fc9d60-d2e1-46de-a273-18b716d27292)

A follow-up question to Q2 regarding multiplicity: If we see the number of multiplicity on one side of an association link that wasn't drawn with navigability (like how `Loan` is represented in the screenshot under Q2 in my previous comment, does that mean that there is navigability too? In other words, if we see a number should there be a reference from the base class? 

</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/33#issuecomment-2408987970" expanded>
<div slot="header">

**14 :fas-comment:**
</div>

Here's a diagram for the last question. Does the one on top imply the one on the bottom?
![image](https://github.com/user-attachments/assets/c2a61467-4c78-4447-b764-58c3f9554019)

</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/33#issuecomment-2409021923" expanded>
<div slot="header">

**15 :fas-comment:**
</div>

I understand, thank you Prof!
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/41#issuecomment-2453053940" expanded>
<div slot="header">

**16 :fas-comment:**
</div>

Thanks for the reassurance Prof!

> Instead of extending from ArrayList, [why not make it into a composition/aggregation](https://www.geeksforgeeks.org/favoring-composition-over-inheritance-in-java-with-examples/) where ArrayList is inside of a class that manages Author list?

As for this, we initially did exactly that. We had an `ArrayList&lt;T>` inside our `AuthorList` class. But we found that it was troublesome to keep making trivial methods to add and remove items from the private `ArrayList` (I think this happened when we wanted to create our second list class). So, we just made it inherit from `ArrayList` so we could use its add and remove methods as-is. More complicated methods were then added to extend the functionality of the `ArrayList`. 

But then again, I guess having those trivial wrapper methods can help with method readability when using them outside. We were lazy at the moment 😃
</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 2. AJAY..NKER `@AjayShanker-geek` (10 posts) <span class=text-warning>:octicon-eye:</span>
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/52" expanded>
<div slot="header">

**1. :fas-info-circle: No valid Tester Response was found**
</div>

Error: `No valid Tester Response was found. Please contact the teaching team for assistance.`

Only logical reason is that I submitted the bug at 6:01pm

<img width="1909" alt="Screenshot 2024-11-20 at 4 41 40 PM" src="https://github.com/user-attachments/assets/09b0bba3-b940-40f1-ba8e-1beea83310c3">

</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/29" expanded>
<div slot="header">

**2. :fas-info-circle: Request for use of Jackson Core Library**
</div>

## Library

[Jackson Databind](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind)
[Jackson Core](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-core)

## Purpose

Our team is planning to use Jackson Databind and Core to serialize and deserialize (JSON &lt;-> Object) for the parser part and try out the generator abstractions. This will make saving and loading user data more efficient and manageable. 

## License

Apache License 2.0 https://www.apache.org/licenses/LICENSE-2.0

</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/2#issuecomment-2293390592" expanded>
<div slot="header">

**3 :fas-comment:**
</div>

Another alternative method is that you could try installing through [homebrew](https://brew.sh) on mac.

```sh
# install homebrew package manger
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# install sourcetree app
brew install --cask sourcetree

# open app
open -a "Sourcetree" # or open normally
```

Edit: Add homebrew url
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/2#issuecomment-2295511976" expanded>
<div slot="header">

**4 :fas-comment:**
</div>

@kennethSty If you wanna try something else, TUI will be inbetween CLI & GUI. I personally use [lazygit](https://github.com/jesseduffield/lazygit) + neovim. 

If I am not wrong, Github Student Developer Pack will give free licence to [GitKraken](https://www.gitkraken.com/) which is GUI app. [LINK](https://education.github.com/pack)

Edit: Add link to Github education 
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/1#issuecomment-2301639273" expanded>
<div slot="header">

**5 :fas-comment:**
</div>

Should the `else` in the table be `0.0` or we need to account this? Link [here](https://nus-cs2113-ay2425s1.github.io/website/schedule/week2/topics.html#key-exercise-grade-helper)


<img width="817" alt="image" src="https://github.com/user-attachments/assets/6ab1a88b-897b-4a9d-8790-331d6c0492fd">

</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/1#issuecomment-2303622449" expanded>
<div slot="header">

**6 :fas-comment:**
</div>

Noted, thanks Prof!
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/44#issuecomment-2461235063" expanded>
<div slot="header">

**7 :fas-comment:**
</div>

This is the preview of us using the theme. [Link:](https://ay2425s1-cs2113-t11-1.github.io/tp/)

<img width="1728" alt="Screenshot 2024-11-07 at 11 14 49 AM" src="https://github.com/user-attachments/assets/c77ac152-ae11-4765-8c0f-d3c7e42b75ed">

</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/48#issuecomment-2469726958" expanded>
<div slot="header">

**8 :fas-comment:**
</div>

Got into the same issue, git will not pickup the changes by just renaming it.

Fix:
```
git config --global core.ignorecase false
git mv <old_name> <new_name>
```
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/48#issuecomment-2473784989" expanded>
<div slot="header">

**9 :fas-comment:**
</div>

Mine is still not being detected. I renamed the file as `ajayshanker-geek.md`
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/48#issuecomment-2487922102" expanded>
<div slot="header">

**10 :fas-comment:**
</div>

@okkhoy Any updates? I did email that team too.
</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 3. STYP..RICH `@kennethSty` (10 posts) <span class=text-warning>:octicon-eye:</span>
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/47" expanded>
<div slot="header">

**1. :fas-info-circle: Submission of TP**
</div>

Is one person per team enough to submit the DG, UG, and jar?
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/22" expanded>
<div slot="header">

**2. :fas-info-circle: Testing code style conformity**
</div>

Is it possible to use the grader's coding style checker before submitting the final version of the IP to ensure nothing is overseen? 

Would be very helpful!


</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/13" expanded>
<div slot="header">

**3. :fas-info-circle: Admin Repo Link Week 4 not working**
</div>

The [invitation link](https://github.com/orgs/nus-cs2113-AY2425S1/invitation.) in [the admin page of week 4 ](https://nus-cs2113-ay2425s1.github.io/website/schedule/week4/admin.html)to the org that we should join is not working:
<img width="1426" alt="image" src="https://github.com/user-attachments/assets/28edcf15-10a7-4d96-a03f-94b33288567e">

</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/12" expanded>
<div slot="header">

**4. :fas-info-circle: Exercise 4.3: Ouput identical with expected output but testcase failed**
</div>

The expected output of the task:
78
12
314
78
12
314
16

My output:
<img width="347" alt="image" src="https://github.com/user-attachments/assets/3a66d8c7-9404-44b2-a419-5e9f25c60223">

Why do I fail this test case? Are any specific whitespaces required? For reference: I print the area directly via System.out.println(s.area())


</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/2" expanded>
<div slot="header">

**5. :fas-info-circle: Sourcetree cannot be opened on Mac**
</div>

Translated Error Message when trying to open Sourcetree: 
_‘Sourcetree’ cannot be opened because Apple cannot search for malware in it.
This software needs to be updated. Contact the developer for more information._

Original Error Screenshot: 
<img width="302" alt="image" src="https://github.com/user-attachments/assets/7d3c9f88-efe6-4537-8db8-d7d0b8968679">


Machine Details: 

- MacOS BigSur
- Version: 11.5.2
- Chip: Apple M1
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/2#issuecomment-2294536997" expanded>
<div slot="header">

**6 :fas-comment:**
</div>

Thanks Ajay! Unfortunately, I get the same error message. 
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/2#issuecomment-2294562171" expanded>
<div slot="header">

**7 :fas-comment:**
</div>

Is it ok if I use the command line instead? 
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/2#issuecomment-2298191500" expanded>
<div slot="header">

**8 :fas-comment:**
</div>

Thanks everyone! I will stick to the Command Line then.
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/22#issuecomment-2370428024" expanded>
<div slot="header">

**9 :fas-comment:**
</div>

Great thanks! @okkhoy how can I use this? &hat;&hat;
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/22#issuecomment-2378368458" expanded>
<div slot="header">

**10 :fas-comment:**
</div>

Thanks! 
</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 4. CHEN..ANDY `@averageandyyy` (9 posts) <span class=text-warning>:octicon-eye:</span>
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/35" expanded>
<div slot="header">

**1. :fas-info-circle: Questions from Lecture on 11/10/2024**
</div>


Hi Prof, in the most recent lecture where we inferred that `ActionX` and `ActionY` were concrete classes and thus would have implemented both `perform()` and `repeat()`, their return types were not specified in their box. Should they have been `perform(): void` and `repeat(): void` instead?

Additionally, while I understand the dependency and reference between the `ActionFactory` and the `Action`s it would create, I am not confident that using a solid line to represent `ActionFactory`'s reference to `History` makes the most sense. One might argue that `History` can be a dependency in the sense that it is possible for us to pass `History` as a parameter to `ActionFactory` for the addition to occur. It is unclear, based on the instructions alone, that `ActionFactory` would contain a `History` instance. Would a dashed arrow indicating dependency in the form of a parameter be also an acceptable answer?

Thanks for the help!
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/23" expanded>
<div slot="header">

**2. :fas-info-circle: Usage of final variables**
</div>


Hi Prof, I understand for constants we can use `public static final String MESSAGE` (as an example) to denote that this is a constant for better readability and reusability. Occasionally however, IntelliJ prompts that certain `private` variables can also be made `final`. Firstly, why does it do that and is there any merit to doing so? Is it due to some optimizations knowing that that variable would not be altered anymore? Secondly, in line with the class' coding standards, are we required to capitalize these variables? i.e. `private final String name = "name"` to `private final String NAME`

Thank you for the help!
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/21" expanded>
<div slot="header">

**3. :fas-info-circle: Request for use of Apache Commons CLI (tP)**
</div>

## Library

Apache Commons CLI https://commons.apache.org/proper/commons-cli/

## Purpose

In our project, we plan to use simple flags such as `-d` and `-q` to simplify user commands. We plan to make use of the aforementioned library to better handle these flags from user input. The library is free, open-source and can be integrated into the project with Gradle/Maven.

## License

Apache License 2.0 https://www.apache.org/licenses/LICENSE-2.0

The relevant links are [Apache Commons CLI](https://commons.apache.org/proper/commons-cli/) and [Apache Commons](https://commons.apache.org/)

</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/6" expanded>
<div slot="header">

**4. :fas-info-circle: Tagging at the end Vs. Tagging incrementally**
</div>


Dear teaching team, as I was working through the iP, I decided to complete all the levels in 1 go and forgot to tag, commit and push incrementally. Can I instead commit and tag just Level 3? Otherwise, I would have to go back to "regress" my work just to execute the incremental commits, which can be quite a hassle. I understand and acknowledge that it is my fault for not reading the instructions clearly. Let me know what I can do in this situation and thank you for your help.

</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/6#issuecomment-2309475505" expanded>
<div slot="header">

**5 :fas-comment:**
</div>

I do not know who the above commenter is. I advise to not click on the suspicious link.
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/6#issuecomment-2309658306" expanded>
<div slot="header">

**6 :fas-comment:**
</div>

Thank you for the reply. Painful lesson learnt!
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/14#issuecomment-2335161310" expanded>
<div slot="header">

**7 :fas-comment:**
</div>

Using the command line, you can check using the `git log` command. The default message would be along the lines of "Merge xx branch"! 

On source tree, you should be able to see the branches merge visually I believe.
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/23#issuecomment-2381348047" expanded>
<div slot="header">

**8 :fas-comment:**
</div>

I tried doing so, but the CS2113 checkstyle is sounding off and saying I should stick to the regular naming conventions as per what I have I been doing, that is, naming `private final` variables like non-constants. Should I proceed to rename them as constants or would it be fine if I preserved the old namings?
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/23#issuecomment-2381359508" expanded>
<div slot="header">

**9 :fas-comment:**
</div>

Will do, thanks for the help Prof! :)
</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 5. LOW ..ERLY `@Bev-low` (6 posts) 
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/36" expanded>
<div slot="header">

**1. :fas-info-circle: Request the use of Mockito Library**
</div>

## Library

[Mockito](https://github.com/mockito/mockito)

## Purpose

In our project, we plan to use Mockito to simulate the behavior of various dependencies and components, making unit testing more efficient and manageable. Mockito is easy to use, free, open-source, and can be easily integrated into our project with Gradle or Maven.

## License

MIT Licence 
https://github.com/mockito/mockito/blob/main/LICENSE

</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/27" expanded>
<div slot="header">

**2. :fas-info-circle: Request for use of Google Gson Library**
</div>

## Library

Gson https://github.com/google/gson

## Purpose

In our project, we plan to use Gson to serialize (convert objects to JSON) and deserialize (convert JSON to objects) various data structures. This will make saving and loading user data more efficient and manageable. The Gson library is easy to use, free, open-source, and can be easily integrated into our project with Gradle or Maven.

## License

Apache License 2.0 https://www.apache.org/licenses/LICENSE-2.0


</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/20" expanded>
<div slot="header">

**3. :fas-info-circle: Question about TP Constraints**
</div>

Hi Prof, 

For our project we plan to have a file store our app data. We're thinking of also exporting a report to a seperate markdown file so there would be two seperate files being mantained by our app. Is it ok to have two files in our local directory at once? Thank you!




</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/8" expanded>
<div slot="header">

**4. :fas-info-circle: Pushed file is not updated**
</div>

Hi I am using Intellij for my Ip project and am trying to push my files into the remote repositary. I used CLI to make commits, make a tag and push. There is a successful push with the tag name. However, when I check my files, there is no update from it. 

When I check my commits using Git Log, I can see that the commits are there. When I check Git Status, it says "Your branch is up to date with 'origin/master'." I did use force commit so my main file in my IP repo is up to date with my code. However, the tagged files are not up to date. I am unsure what is the issue here, my changes are not being saved. 

Link to Level-1 tag https://github.com/Bev-low/ip/releases/tag/level-1
Link to Level-0 tag https://github.com/Bev-low/ip/releases/tag/level-0
Both tags contains the same files

Thank you for your help. 

</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/8#issuecomment-2318349559" expanded>
<div slot="header">

**5 :fas-comment:**
</div>

Oh it works now, thank you so much!
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/36#issuecomment-2424745864" expanded>
<div slot="header">

**6 :fas-comment:**
</div>

Hi Prof, sorry to bother on a weekend, just wanted to check in on this.
</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 6. XION..UANG `@ThisisXXZ` (5 posts) <span class=text-warning>:octicon-eye:</span>
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/49" expanded>
<div slot="header">

**1. :fas-info-circle: Making PE Response on GitHub**
</div>

&gt;!--Remember to give sufficient details e.g.,
* Your development environment (IntelliJ version, Java version, OS, ...)
* Relevant code, error message, stack trace
* Relevant code snippet (an example given below), or link to the relevant code on your GitHub repo

```java
String value = "Some code here"
```

You can use Markdown to format your text. See https://guides.github.com/features/mastering-markdown/

Remember to close the issue after your problem is resolved.

Delete these instructions before posting.-->

Sorry I've made two responses on GitHub, and it seems that the Catcher cannot parse them.
Could you kindly help me with that?
The two faulty responses are:
* https://github.com/nus-cs2113-AY2425S1/pe-dev-response/issues/348
* https://github.com/nus-cs2113-AY2425S1/pe-dev-response/issues/405

Thank you so much!
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/18" expanded>
<div slot="header">

**2. :fas-info-circle: How to access the weekly post-lecture quiz?**
</div>


Has it been released yet?
Thanks!
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/10" expanded>
<div slot="header">

**3. :fas-info-circle: Unable to Join GitHub Organization**
</div>

The invitation link on the course website does not seem to work for me.
![image](https://github.com/user-attachments/assets/042a4bfa-f41a-435c-996c-87a611419ebc)
Is anyone facing the same problem or is it because my account hasn't been registered for this course?

</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/10#issuecomment-2320818905" expanded>
<div slot="header">

**4 :fas-comment:**
</div>

> we haven't sent the invitations yet!!

Got it. Thanks, professor!
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/49#issuecomment-2482127178" expanded>
<div slot="header">

**5 :fas-comment:**
</div>

Problem solved. Thanks!
</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 7. HUYN..LINH `@DanLinhHuynh-Niwashi` (4 posts) <span class=text-warning>:octicon-eye:</span>
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/4" expanded>
<div slot="header">

**1. :fas-info-circle: 💡Resolve unable to push due to Authentication Failed: Support for password authentication was removed on August 13, 2021.**
</div>

If you're having the following trouble and have tried all the usual methods, here's a workaround:
![image](https://github.com/user-attachments/assets/b5e0844b-a0aa-4b8c-a7ee-e4f8e9d3c398)

Using PAT (Personal Access Token) to push new commits on your repo.
1. **Create Your PAT**: Follow the instructions in this [link](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic).
2. **Store Your PAT**: Copy your token and save it securely on your computer.
3. **Update Your Remote URL**: Open your repo in Git Bash and run the following command:
`git remote set-url origin https://&lt;USERNAME>:&lt;PAT>@github.com/&lt;USERNAME>/&lt;REPO NAME>.git`

I'm still working on a permanent solution to this problem. If anyone has any suggestions or clues, please let me know. Thank you!
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/3#issuecomment-2306147933" expanded>
<div slot="header">

**2 :fas-comment:**
</div>

I think it should be okay, the session will be opened on time (it did last week). That might be some kind of bugs on Archipelago i guess.
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/12#issuecomment-2323977611" expanded>
<div slot="header">

**3 :fas-comment:**
</div>

There is no white space required, I just directly printed it out just like you.

You may check if your output has an extra return or sth like that?

</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/12#issuecomment-2323987976" expanded>
<div slot="header">

**4 :fas-comment:**
</div>

If the program was successfully built, i think this may not the case.

As you store all of your instances in a list/ array of type Shape.
</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 8. LEON..SPER `@ryryry-3302` (3 posts) <span class=text-warning>:octicon-eye:</span>
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/19" expanded>
<div slot="header">

**1. :fas-info-circle: Regarding submission of UG on canvas**
</div>

Hi may I know where the submission link can be found on canvas for this [deliverable](https://nus-cs2113-ay2425s1.github.io/website/schedule/week6/project.html#2-draft-the-ug-midnight-before-the-tutorial)
![image](https://github.com/user-attachments/assets/8dd2ca5b-29fb-4098-9cea-d95874963f5f)

</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/2#issuecomment-2294732154" expanded>
<div slot="header">

**2 :fas-comment:**
</div>

@kennethSty If im not wrong prof mentions that using entirely through CLI is fine over [here](https://nus-cs2113-ay2425s1.github.io/website/schedule/week1/admin.html#tool-git-for-revision-control) under Admin Tools - Git

You can find instructions on the command line setup [here](https://nus-cs2113-ay2425s1.github.io/website/schedule/week2/topics.html#tools-git-and-github-init-getting-started)

This disclaimer is also found at the bottom 2.7c
![image](https://github.com/user-attachments/assets/e3ffce99-65ce-4418-8a77-0e23c7c5aee0)

</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/19#issuecomment-2350931434" expanded>
<div slot="header">

**3 :fas-comment:**
</div>

I see thank you 
</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 9. ANDE..HENG `@Holy-An` (2 posts) 
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/51" expanded>
<div slot="header">

**1. :fas-info-circle: Error in parsing tester response**
</div>

Hi, I have a faulty issue and was told to approach the teaching team for help. The faulty issue is regarding the history command in my pe repo. There is nothing I could revert on github. 

![image](https://github.com/user-attachments/assets/8fa574e8-f8ca-40c7-813c-594aa3952dec)

</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/51#issuecomment-2488842368" expanded>
<div slot="header">

**2 :fas-comment:**
</div>

I selected 7 bugs, and initially it was not faulty. Nevertheless, does this mean this bug is now invalid? 
</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 10. KODE..JITH `@KSanjith` (2 posts) 
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/34" expanded>
<div slot="header">

**1. :fas-info-circle: Used-JUnit tag changed from green to red**
</div>

Every member of the group CS2113-W13-1 had authored JUnit tests individually and successfully merged their PRs, which turned the Used-JUnit tag on all of their individual tp dashboards green. However, after a group member re-packaged the J-Unit files (without altering the code) and merged that PR, the JUnit tags for all the other group members turned red. We would like to ask how we can rectify this issue and return the tag to green?
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/24" expanded>
<div slot="header">

**2. :fas-info-circle: Question about A-MoreOOP increment**
</div>

Dear Prof and TAs, I would like to ask whether it is **compulsory to create new Ui and Storage objects** in Main, and use those objects throughout the rest of the iP? Or instead, can the **Ui and Storage classes comprise purely of static methods** that are called as and when needed, **without** having to create the Ui and Storage objects and passing them around? Thank you.
</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 11. RYAN.. TAN `@ryan-txn` (2 posts) 
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/45" expanded>
<div slot="header">

**1. :fas-info-circle: Clarification on TP Constraint-Single-User & Multiple Instances by Same User**
</div>

Hi all, my team would like to clarify if Constraint-Single-User for the TP applies to a single user running the application in two instances? We are unsure how to handle this scenario raised as a Bug in the PE Dry Run (inability to update both instances with correct information).
TP constraint:
![image](https://github.com/user-attachments/assets/56885cab-a229-44c3-bd28-a2de2c22b9bd)
Example of 1 user having multiple instances:
![image](https://github.com/user-attachments/assets/8111d6f4-ed04-4ef7-9104-6abc3775e4f7)
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/45#issuecomment-2466604052" expanded>
<div slot="header">

**2 :fas-comment:**
</div>

> Sorry, I don't understand the issue or the bug report. What about opening 2 instances?

Is opening 2 instances at the same time in violation of the project constraints?
</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 12. ATUL..ALLI `@Atulteja` (2 posts) 
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/40" expanded>
<div slot="header">

**1. :fas-info-circle: JUnit Testing for toString and equals functions**
</div>

for toString and equals functions do we have to write JUnit tests? 
![image](https://github.com/user-attachments/assets/84fee275-3ab5-406c-8ce5-0ac35a74c74b)



</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/7" expanded>
<div slot="header">

**2. :fas-info-circle: Making changes to code after pushing tags**
</div>

I have completed my iP part for the week 3 but i realised i need to make some changes to one of the tags. So do i just make the changes and push to github wihtout tagging or do i have to edit the commit which the tag is linked to?

</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 13. SARA..XUAN `@sarahchow03` (2 posts) 
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/26" expanded>
<div slot="header">

**1. :fas-info-circle: Preferred way to add JUnit tests to repository**
</div>

If I have submitted a pull request for a particular feature and closed the issue, but have yet to write JUnit tests for it, is there a standard convention for me to follow to add said JUnit tests into the repository?

For instance, submit an issue "JUnit tests for add member function", and submit a PR for the issue for JUnit tests only.
Moving forward, is it better for me to do all tests and documentation in its related issue? Or is splitting them up into smaller increments (issues) a better strategy?
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/26#issuecomment-2397211754" expanded>
<div slot="header">

**2 :fas-comment:**
</div>

Thank you Prof! Will take note of this.
</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 14. ZHAI..HONG `@YukeeHong` (2 posts) 
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/48" expanded>
<div slot="header">

**1. :fas-info-circle: ppp file name**
</div>


<img width="408" alt="image" src="https://github.com/user-attachments/assets/892ce9d5-3e5f-43c6-a0f4-cbed45df09ab">

just find this, upload on week 11 but forget to change file name to lower case. is there any makeup way?
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/30" expanded>
<div slot="header">

**2. :fas-info-circle: Wrongly merge the tp code  from the master branch of my branch**
</div>

Will the contribution still be counted?
If not, what can I do to make up for it
</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 15. YU M.. KIT `@Toby-Yu` (2 posts) 
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/14" expanded>
<div slot="header">

**1. :fas-info-circle: About merge without fast forward**
</div>

I want to ask how can I check if my merge is done without fast forward after i finish the action? Is it visible in Git or Sourcetree? Or is there anythings I can observe to make sure my merge is correctly done without fasr forward?

</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/5" expanded>
<div slot="header">

**2. :fas-info-circle: some of my files disapper after i open th the project in Intellij IDEA**
</div>


https://github.com/user-attachments/assets/8077d109-c6d6-40ae-ab23-f9c0f018736b

this is the situation i am facing.
</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 16. TRAN..HONG `@Sukkaito` (2 posts) 
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/46" expanded>
<div slot="header">

**1. :fas-info-circle: Claiming authorship for tP during code-freeze period**
</div>



Hello Professor Akshay,

For the past few weeks, we have been coding nonstop to deliver the best tP we possibly can. But one thing, we haven't claimed any authorship for ourselves (probably since the beginning), which could heavily affect correctness and performance of RepoSense. 

_**Question:**_
> Can we get the permission to claim the authorship (which will require editing the code) after the final v2.1 deliverables deadline? Or we will have to spend some time to do so before the deadline?

Thank you and have a good day! :D
</panel>

<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/3#issuecomment-2306188636" expanded>
<div slot="header">

**2 :fas-comment:**
</div>

I have the same problem too, for now I'll probably just create a rule for Outlook to move invitations to a folder/subfolder.

FYI, create a new folder on Outlook, go to ```Settings -&gt; Rules -&gt; Add new rule```. Filter all emails from noreply@archipelago.rocks and remember to tick "Run rule now" (Modify the exception and different settings if you want). Then ```Save```.

All the invitation emails should go to the folder you've created, just remember to pin or put it somewhere for you to know if there is any update.

![image](https://github.com/user-attachments/assets/b7f56b82-212c-4f05-b589-2ad333b5132d)

</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 17. SI T..AUNG `@C2linaung` (1 posts) 
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/43" expanded>
<div slot="header">

**1. :fas-info-circle: Request to use Zip4j (& clarification)**
</div>

## Library

[Zip4j](https://mvnrepository.com/artifact/net.lingala.zip4j/zip4j/2.11.5)

## Purpose

To created password protected zip files and store it as backup. 

I understand that there is a constraint on human-editable file. What I want to do is to have 2 separate folders. 1 to store the data files and another to store the backup. So technically, I am still allowing users to manipulate the data by editing the data files since data is still being loaded from the data folder which is not encrypted (only the backup folder is encrypted - in the event that users corrupted the data file and want to restore the previously saved copy). 

Is this allowed?

## License

[LICENSE](https://www.apache.org/licenses/LICENSE-2.0.txt)

</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 18. GAO ..NING `@Gao327` (1 posts) 
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/9" expanded>
<div slot="header">

**1. :fas-info-circle: Use of external software (integrating llm to the ip)**
</div>


I have an idea of adding some extension feature to the ip on top of the required increments to make the software more interesting. One option is adding a large language model. One way is using Hugging Face Transformers + Inference API (Free Tier), or other free, open-sourced models. Another option is using a local light weight library such as llama.cpp.
I wish to know if these ideas are accepted. Thanks!
</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 19. LEE .. ZHE `@ehz0ah` (1 posts) <span class=text-warning>:octicon-eye:</span>
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/38" expanded>
<div slot="header">

**1. :fas-info-circle: Request to use OpenCSV & Jackson Library**
</div>

## Library

[OpenCSV](https://opencsv.sourceforge.net)
[Jackson](https://github.com/FasterXML/jackson)

## Purpose

OpenCSV is used to parse CSV file while Jackson is used for parsing JSON files.

## License

[Jackson's License](https://www.apache.org/licenses/LICENSE-2.0.txt)
[OpenCSV's License](https://www.apache.org/licenses/LICENSE-2.0.txt)

</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 20. GOH ..REMY `@jemehgoh` (1 posts) <span class=text-warning>:octicon-eye:</span>
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/12#issuecomment-2323980936" expanded>
<div slot="header">

**1 :fas-comment:**
</div>

Check your code for the Rectangle() and Circle() classes on Coursemology. Did you inherit from the Shape() class? (I had this problem with this exercise)
</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 21. LIM ..KIAT `@limkongkiat` (1 posts) 
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/31" expanded>
<div slot="header">

**1. :fas-info-circle: Issue with iP final submission**
</div>

Hi Prof,

I received an email saying that my JAR file could not be found.
![image](https://github.com/user-attachments/assets/c9a775e3-1cdf-438b-96b4-a048690aee65)

However, the JAR file can be accessed through the link stated in the email.
![image](https://github.com/user-attachments/assets/dde700d6-1c3a-480d-8781-65cc436bcd83)

May I know what I need to do to rectify the issue?

Thank you!


</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 22. NG C..FONG `@NCF3535` (1 posts) <span class=text-warning>:octicon-eye:</span>
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/44" expanded>
<div slot="header">

**1. :fas-info-circle: Request to use just-the-docs templete**
</div>

## Library

[just-the-docs](https://github.com/just-the-docs/just-the-docs)

## Purpose

We intend to use this template to create documentation for our project. It provides a simple, clean, and responsive design that is easy to navigate, which will improve the accessibility and readability of our project’s documentation. It includes features such as search functionality, sidebar navigation, and customizability, which would enhance the overall user experience.

## License

The library is released under the MIT License. More details can be found [here](https://opensource.org/license/MIT).

</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 23. DHAS..HNAA `@DarkDragoon2002` (1 posts) 
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/50" expanded>
<div slot="header">

**1. :fas-info-circle: tp PE: Dev Team Referenced Prof, would like to clarify if accurate**
</div>

Hi Prof, would like to check and clarify to see if you said the following below to team W10-2 as they quoted you in their Dev Response. 

Their app in it's current state does not allow for adding of custom entries and only allows additions that match a pre-defined list.

I believe it is not enough functionality for tp requirements and even if it is, as a CEG student who has applied for SEP (their target user as identified in their DG) not having custom entry capabilities is very debilitating. In fact most of my peers mapped mods outside the small selection provided. Hence, I would think this is an important part that should be included. They also only mentioned this limitation in their FAQs in their UGs and not under the add command section.

They have quoted you in their defense to term this as `severity.Low` and `type.NotInResponse` from `severity.High`. Would just like to confirm if what they stated was true and some guidance on this matter. Thanks!

Screenshots for your reference.
![image](https://github.com/user-attachments/assets/bc71d44a-1f98-490f-8fa4-e182c8448a91)

![image](https://github.com/user-attachments/assets/657b98fb-6bdd-41bf-a75b-f66019772a58)

</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 24. NGUY..HONG `@DucPhong135` (1 posts) 
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/17" expanded>
<div slot="header">

**1. :fas-info-circle: Problem regarding late tagging for iP**
</div>

So the deadline for level-4 iP is last week, and I have push all of the code for week 4 iP before that deadline. However, when I checked today, the tag for level-4 and A-CodeQuality disappeared from my commit. I have push back the tag today but my tracking is red now, is there any way for me to solve that?

</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 25. JOE .. YOU `@louisjoety` (1 posts) <span class=text-warning>:octicon-eye:</span>
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/28" expanded>
<div slot="header">

**1. :fas-info-circle: Request for use of glassfish.json and javax.json Library**
</div>

## Library

org.glassfish.json:1.1.4
[org.glassfish.json](https://mvnrepository.com/artifact/org.glassfish/javax.json/1.1.4)

javax.json.json-api:1.1.4
[javax.json-api](https://mvnrepository.com/artifact/javax.json/javax.json-api/1.1.4)

## Purpose

I wish to use this library to handle JSON processing in the project, including but not limited to parsing and querying JSON data.

## License

Both libraries are released under the [CDDL+GPL 1.1 License](https://oss.oracle.com/licenses/CDDL+GPL-1.1).
</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 26. CHAN..ENCE `@Hackin7` (1 posts) 
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/39" expanded>
<div slot="header">

**1. :fas-info-circle: Inquiry about Week 11 deadlines**
</div>

In the schedule, it was stated that we were given 2 weeks to finish Week 11 tasks, so we can finish them by Week 12 lecture timeslot/ given deadline whichever is earlier. Does this include the badges on the dashboard?

![image](https://github.com/user-attachments/assets/7bd47465-07d6-4bcc-8a97-7130b423f465)


</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 27. ALFR.. GOH `@Alfred-Goh02` (1 posts) 
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/37" expanded>
<div slot="header">

**1. :fas-info-circle: Request the use of XChart Library**
</div>

## Library

[XChart](https://knowm.org/open-source/xchart/)

## Purpose

It is a free-to-use, lightweight open source Java Library for plotting data. We plan to use this library to generate trend graph for users in our app that is more accurate and easy to read than text-based charts/graphs, and can be easily integrated into the project with Gradle.

## License

Apache License [https://github.com/knowm/XChart?tab=Apache-2.0-1-ov-file](https://github.com/knowm/XChart?tab=Apache-2.0-1-ov-file)

</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 28. NIRA..INGH `@nirala-ts` (1 posts) <span class=text-warning>:octicon-eye:</span>
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/15" expanded>
<div slot="header">

**1. :fas-info-circle: concerns about tP**
</div>

Hello! Can we use json or CSV files to store and retrieve data from them for our tP? Thank you.
</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 29. VENK..INDA `@mayfairmi6` (1 posts) <span class=text-warning>:octicon-eye:</span>
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/42" expanded>
<div slot="header">

**1. :fas-info-circle: Request the use of Exchangerates API**
</div>

## Library

[exchangerates](https://exchangeratesapi.io)

## Purpose

To add support for converting currencies in real time so that the user would be able to track their budget in their home currency when travelling/making purchases through overseas channels

## License

MIT License. Source: https://github.com/exchangeratesapi/exchangeratesapi/blob/master/LICENSE

</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 30. ZHAN..CORA `@coraleaf0602` (1 posts) <span class=text-warning>:octicon-eye:</span>
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/16" expanded>
<div slot="header">

**1. :fas-info-circle: creating branch-A-Packages**
</div>


Hello!

As part of the iP for this week, do we create the branch-A-Packages off our master branch or the newly created branch-Level-5?

Thank you!
</panel>

</panel>


<panel type="info"  collapsed>
<div slot="header">

### 31. FU Y..XUAN `@MatchaRRR` (1 posts) 
</div>


<panel  popup-url="https://github.com/nus-cs2113-AY2425S1/forum/issues/32" expanded>
<div slot="header">

**1. :fas-info-circle: Issue with iP final submission**
</div>

Hi prof. I received an email saying that my jar file is not available. but it can be accessed and downloaded from the website. I wonder what I need to do to rectify the issue.
![屏幕截图 2024-10-12 013449](https://github.com/user-attachments/assets/eb85d25a-8031-4f82-911e-5f72d4186807)


</panel>

</panel>
