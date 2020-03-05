## Installing and running

To run the naan factory do the following:

```python
import naan_factory
run factory()
```

### TDD - test driven development

1. Write the test
2. Run it, and read the error
3. Code and make it pass the test

This helps with:

- Stop over engineering
- Maintainable code
- Reduce technical debt
- Goes well with agile and working code
- Errors can be your guid in complex systems

How it works is that we write the unit tests.

#### Unit Tests

Test single pieces of code. Like a function.

**base of a test**
Usually has 3 phases.
- setup phase (know variables)
- calling of the function / piece of code with known variables
- asserting for expect output

#### User stories for Naan Factory
```
#1
As a user, I can use the make_dough with water and flour to make dough.

#2
As a user, I can use the bake_dough with dough to get naan.

#3
