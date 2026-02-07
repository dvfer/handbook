import marimo

__generated_with = "0.19.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import marimo as mo
    return mo, pd


@app.cell
def _(mo):
    mo.md(r"""
    ### 175
    """)
    return


@app.cell
def _(pd):
    data = [[1, 'Wang', 'Allen'], [2, 'Alice', 'Bob']]
    person = pd.DataFrame(data, columns=['personId', 'firstName', 'lastName']).astype({'personId':'Int64', 'firstName':'object', 'lastName':'object'})
    data = [[1, 2, 'New York City', 'New York'], [2, 3, 'Leetcode', 'California']]
    address = pd.DataFrame(data, columns=['addressId', 'personId', 'city', 'state']).astype({'addressId':'Int64', 'personId':'Int64', 'city':'object', 'state':'object'})
    return address, person


@app.cell
def _(address, mo, person):
    _df = mo.sql(
        f"""
        SELECT person.firstName, person.lastName, address.city, address.state from person LEFT JOIN address ON address.personId = person.personId
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### 176. Second Highest Salary
    """)
    return


@app.cell
def _(pd):

    employee = pd.DataFrame( [[1, 100], [2, 200], [3, 300]], columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
    return (employee,)


@app.cell
def _(employee, mo):
    _df = mo.sql(
        f"""
        select DISTINCT salary from employee order by salary desc limit 1 offset 1
        """
    )
    return


@app.cell
def _(employee, mo):
    _df = mo.sql(
        f"""
        SELECT MAX(salary) AS SecondHighestSalary FROM employee WHERE salary != (SELECT MAX(salary) as highestSalary FROM employee)
        """
    )
    return


@app.cell
def _(employee, mo):
    _df = mo.sql(
        f"""
        SELECT 
        MAX(salary) AS SecondHighestSalary
        FROM employee
        WHERE salary < (SELECT MAX(salary) FROM employee);
        """
    )
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 177. nth highest salary
    """)
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
        BEGIN
          -- Perform the math here, before the query
          SET N = N - 1;

          RETURN (
              SELECT DISTINCT salary 
              FROM employee 
              ORDER BY salary DESC 
              LIMIT 1 OFFSET N
          );
        END
        """
    )
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 178. Rank Scores
    """)
    return


@app.cell
def _(pd):
    data_178 = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
    scores = pd.DataFrame(data_178, columns=['id', 'score']).astype({'id':'Int64', 'score':'Float64'})
    return (scores,)


@app.cell
def _(mo, scores):
    _df = mo.sql(
        f"""
        select
        	score,
            DENSE_RANK() OVER (
            	order by score desc
            ) as rank 
            from scores
        """
    )
    return


@app.cell
def _():
    return


@app.cell
def _(pd):
    data_180 = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]
    logs = pd.DataFrame(data_180, columns=['id', 'num']).astype({'id':'Int64', 'num':'Int64'})
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT
            count(num) as conteo over (partition)
        from logs  


        """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
