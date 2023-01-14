from flask import Flask, request

@app.route('/')

def calculator():
    return '''
        <form method="POST" action="/calculate">
            <input type="text" name="num1" placeholder="Number 1">
            <input type="text" name="num2" placeholder="Number 2">
            <select name="operator">
                <option value="add">+</option>
                <option value="subtract">-</option>
                <option value="multiply">*</option>
                <option value="divide">/</option>
            </select>
            <br><br>
            <input type="submit" value="Calculate">
        </form>
    '''


