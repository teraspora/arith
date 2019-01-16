# Arith

## Specification

This application is designed to fulfil the requirements of the third milestone project of the Code Institute Full Stack Developer course 2018.

It is a simple game in which the user practises her/his mental arithmetic by attempting to calculate sums, differences, products and quotients of positive integers.  Multiple users are catered for, and the app keeps track of how many questions each user has attempted, and how many have been answered correctly.   It is able to pass this data to HTML templates which are styled with CSS and thus displayed to each user in the browser.

Each user will see a leaderboard that ranks top scores for all users, as well as their own performance data.

In accordance with project guidelines, there is no persistence of data.   All information is held in volatile memory.   Similarly, there is no security or user validation.

The application uses Flask for routing and templating, and will be deployed to Heroku.   All logic is implemented in Python on the server.   Javascript on the client machine is used only for callbacks on text input etc.

We define three classes: User, Q and Op, representing the user, question and current operator (+, -, * or /) respectively.

We define a range for the operands (2 to n), initially fixed, later user-set.

We use an <input> element on the page for the user to type in their answer.  They will then be congratulated or commiserated with and subsequently will proceed to attempting to answer the next randomly-generated arithmetic problem.   Their score and relative standing will be updated.

In version 0.0 n will be 16 and we won't allow division!

In version 0.01 there will be an "Exit" button with suitable functionality.

In version 0.1 the user will be able to select the range.

In version 0.2 we will allow division!   This involves dealing with non-integers, algebraic irrationals, protecting against division by zero.

In version k, where k > 0, the proverbial sky is the limit as k tends to infinity. ;)

## Testing

Once the basic framework is set up, a TDD approach will be adopted.

Tests will be created to check the logic regarding validation of user input, checking arithmetic operations and maintaining and updating user data.

The simple interface will lend itself to responsive design, so the application will be usable on mobile without difficulty.   I note, though, that the more features I introduce, the more danger of the UI becoming cluttered.

Manual tests on different devices will also be necessary.
