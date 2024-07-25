from flask import Flask

app = Flask(_name_)

@app.route('/home')
def home():
    return('''<html><body><h1> 
gallery! </h1>

<p> <a href="/food1"> first food picture</a> </p>
<p> <a href="/food2"> second food picture</a> </p>
<p> <a href="/food3"> third food picture</a> </p>

<p> <a href="/pet1"> first pet picture</a> </p>
<p> <a href="/pet2"> second pet picture</a> </p>
<p> <a href="/pet3"> third pet picture</a> </p>

<p> <a href="/space1"> first space picture</a> </p>
<p> <a href="/space2"> second space picture</a> </p>
<p> <a href="/space3"> third space picture</a> </p>

     </body></html''')

@app.route('/food1')

def food1():
    return ('''

          <p> <a href="/home"> home </a> </p>
          <p> <a href="/food2"> food2 </a> </p>
          <p> <a href="/food3"> food3 </a> </p>

        <html><body> <img src= "https://idaatalaalm.com/wp-content/uploads/2020/04/%D8%A7%D9%84%D9%83%D9%84%D8%A8-%D8%A7%D9%84%D9%82%D9%88%D9%82%D8%A7%D8%B2%D9%8A-1000x580.jpg"alt="dog"></body></html>`"

def food2():
    return ('''
               <p> <a href="/home"> home </a> </p>
        
            <p> <a href="/food1"> food1 </a> </p>
            <p> <a href="/food3"> food3 </a> </p>

        <html><body> <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrm45IT7TPDizgfnHZXQPDqLqTyIxJBt0D4Q&s" alt="Italian Trulli"></body> </html>''')

@app.route('/food3')

def food3():
    return ('''
                                <p> <a href="/home"> home </a> </p>


                       <p> <a href="/food2"> food2 </a> </p>
                       <p> <a href="/food1"> food1 </a> </p>

        <html><body> <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLQzQqVBk7LmMbMSaEuRy3AkVv1lyGqThm4Q&s" alt="Italian Trulli"></body> </html>''')


@app.route('/pet1')

def pet1():
    return (''' <html><body> <p> <a href="/home"> home </a> </p>
                  <p> <a href="/pet2"> pet2 </a> </p>
                  <p> <a href="/pet3"> pet3 </a> </p>
        <html><body> <img src="https://images.unsplash.com/photo-1450778869180-41d0601e046e?q=80&w=1886&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Italian Trulli"></body> </html>''')




                                                                                                          
def pet2():
    return ('''
                <p> <a href="/home"> home </a> </p>
                  <p> <a href="/pet3"> pet3 </a> </p>
                  <p> <a href="/pet1"> pet1 </a> </p>

            <html><body> <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLQzQqVBk7LmMbMSaEuRy3AkVv1lyGqThm4Q&s" alt="Italian Trulli"></body> </html>''')



@app.route('/pet3')

def pet3():
    return ('''


                   <p> <a href="/pet2"> pet2 </a> </p>
                   <p> <a href="/pet1"> pet1 </a> </p>


                  <p> <a href="/home"> home </a> </p>
<html><body> <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpS0-nSwynSihq_bRt18k9kwm95zihQ-yIpg&s" alt="Italian Trulli"></body> </html>''')

@app.route('/space1')

def space1():
    return ('''

                <p> <a href="/home"> home </a> </p>
                <p> <a href="/space2"> space 2 </a> </p>
                <p> <a href="/space3"> space 3 </a> </p>


        <html><body> <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_jhAAgM3oQaQTjXtWENyTCpya9-b2WLIpig&s" alt="Italian Trulli"></body> </html>''')

@app.route('/space2')

def space2():
    return ('''

                <p> <a href="/home"> home </a> </p>
                <p> <a href="/space3"> space 3  </a> </p>
                <p> <a href="/space1"> space 1 </a> </p>


<html><body> <img src="https://static.scientificamerican.com/sciam/cache/file/46D6B298-77D1-4CB6-A89EED69EEE6EED2_source.jpg?w=1200" alt="Italian Trulli"> </body> </html>''')

@app.route('/space3')

def space3():
    return ('''


            <p> <a href="/home"> home </a> </p>
            <p> <a href="/space1"> space1 </a> </p>
            <p> <a href="/space2"> space 2</a> </p>

        <html><body> <img src="https://t3.ftcdn.net/jpg/06/37/72/42/360_F_637724214_M6yKVgHI7zaF46PM00ixE7bf1HVwLqpA.jpg" alt="Italian Trulli"></body> </html>''')

    
if _name_ == '_main_':
    app.run(debug=True)
