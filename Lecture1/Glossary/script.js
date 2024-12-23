document.addEventListener("DOMContentLoaded", () => {
  const glossary = [
    {
      term: "assignment",
      definition: "A statement that assigns a value to a variable.",
      icon: "<i class='fas fa-arrow-right'></i>",
      code: "name = 'Fatimah' # assigns Fatimah to name",
    },
    {
      term: "concatenate",
      definition: "To join two operands end to end.",
      icon: "<i class='fas fa-link'></i>",
      code: "'Fatimah' + ' ' + 'Alzahrani' # returns 'Fatimah Alzahani'",
    },
    {
      term: "comment",
      definition:
        "Information in a program that is meant for other programmers (or anyone reading the source code) and has no effect on the execution of the program.",
      icon: "<i class='fas fa-comment'></i>",
      code: "# This is a comment",
    },
    {
      term: "evaluate",
      definition:
        "To simplify an expression by performing the operations in order to yield a single value.",
      icon: "<i class='fas fa-calculator'></i>",
      code: "2 + 3 * 4 # evaluates to 14",
    },
    {
      term: "expression",
      definition:
        "A combination of variables, operators, and values that represents a single result value.",
      icon: "<i class='fas fa-puzzle-piece'></i>",
      code: "discounted_price = price * 0.5  # an expression combining variables, operators, and values",
    },
    {
      term: "floating point",
      definition: "A type that represents numbers with fractional parts.",
      icon: "<i class='fas fa-percent'></i>",
      code: "pi = 3.14 # floating point number",
    },
    {
      term: "integer",
      definition: "A type that represents whole numbers.",
      icon: "<i class='fas fa-arrow-up-9-1'></i>",
      code: "age = 22 # integer number",
    },
    {
      term: "keyword",
      definition:
        "A reserved word that is used by the compiler to parse a program; you cannot use keywords like if, def, and while as variable names.",
      icon: "<i class='fas fa-key'></i>",
      code: "if x > 5 : # 'if' is a keyword ",
    },
    {
      term: "mnemonic",
      definition:
        "A memory aid. We often give variables mnemonic names to help us remember what is stored in the variable.",
      icon: "<i class='fas fa-lightbulb'></i>",
      code: "userEmail = 'Fatimah@gmail.com' # 'userEmail' is a mnemonic name",
    },
    {
      term: "modulus operator",
      definition:
        "An operator, denoted with a percent sign (%), that works on integers and yields the remainder when one number is divided by another.",
      icon: "<i class='fas fa-percent'></i>",
      code: "5 % 2 # returns 1 (remainder of 5 divided by 2)",
    },
    {
      term: "operand",
      definition: "One of the values on which an operator operates.",
      icon: "<i class='fas fa-equals'></i>",
      code: "x + 5 # 'x' and '5' are operands, '+' is the operator",
    },
    {
      term: "operator",
      definition:
        "A special symbol that represents a simple computation like addition, multiplication, or string concatenation.",
      icon: "<i class='fas fa-cogs'></i>",
      code: "x * 5 # '*' is the multiplication operator",
    },
    {
      term: "rules of precedence",
      definition:
        "The set of rules governing the order in which expressions involving multiple operators and operands are evaluated.",
      icon: "<i class='fas fa-random'></i>",
      code: "2 + 3 * 4 # '*' (multiplication) has higher precedence than '+' (addition), so result is 14",
    },
    {
      term: "statement",
      definition:
        "A section of code that represents a command or action. So far, the statements we have seen are assignments and print expression statements.",
      icon: "<i class='fas fa-list'></i>",
      code: "print('Hello, world!') # print statement",
    },
    {
      term: "string",
      definition: "A type that represents sequences of characters.",
      icon: "<i class='fas fa-font'></i>",
      code: "'Python is fun!' # string value",
    },
    {
      term: "type",
      definition:
        "A category of values. The types we have seen so far are integers (type int), floating-point numbers (type float), and strings (type str).",
      icon: "<i class='fas fa-cogs'></i>",
      code: "height = 150 # height is an integer (type int)",
    },
    {
      term: "value",
      definition:
        "One of the basic units of data, like a number or string, that a program manipulates.",
      icon: "<i class='fas fa-database'></i>",
      code: "weight = 30.5 # 30.5 is a value for the weight variable of type float",
    },
    {
      term: "variable",
      definition: "A name that refers to a value.",
      icon: "<i class='fas fa-xmark'></i>",
      code: "x = 10 # 'x' is a variable holding the value 10",
    },
  ];

  const glossaryContainer = document.getElementById("glossary");

  glossary.forEach((item) => {
    const glossaryItem = document.createElement("div");
    glossaryItem.classList.add("glossary-term");
    glossaryItem.innerHTML = `
        <div class="term">${item.icon} ${item.term}</div>
        <div class="definition">${item.definition}</div>
        <div class="code-example"><code><pre>${item.code}</code></pre></div>
      `;
    glossaryContainer.appendChild(glossaryItem);
  });
});

const searchBox = document.getElementById("search-box");
searchBox.addEventListener("input", () => {
  const searchTerm = searchBox.value.toLowerCase();
  document.querySelectorAll(".glossary-term").forEach((term) => {
    const termText = term.querySelector(".term").textContent.toLowerCase();
    term.style.display = termText.includes(searchTerm) ? "block" : "none";
  });
});

glossaryItem.addEventListener("click", () => {
  glossaryItem.classList.toggle("expanded");
});
