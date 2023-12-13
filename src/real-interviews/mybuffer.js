let input = [
    {name: 'Sara', age: 24},
    {name: 'Mario', age:25},
    {name: 'Pablo', age:25},
    {name: 'Julia', age:25},
    {name: 'Jess', age:35 },
    {name: 'Omar', age:31},
    {name:'Mey', age:27}
]


// create a buffer as a set
const myBuffer = new Set()

function emptyBuffer() {
    console.log('emptied!')
    myBuffer.forEach((item)=>{console.log(item)})
    myBuffer.clear()
}

function isNotFull() {
    return myBuffer.size < 5
}


let timeoutNotPassed;


function delay(time) {
    return new Promise(resolve => setTimeout(resolve, time));
} 



// create another timer that will push elements from object
async function startBuffer() {
    timeoutNotPassed = true
    // while timeout has not passed or buffer is not full
    while(isNotFull() && timeoutNotPassed){
        await delay(1000)
        if(input.length>0){
            // insert names to buffer 
            myBuffer.add(input.shift())
            console.log('added!')
        }
        console.log('checking')
    }
    emptyBuffer()
    
    if(input.length>0){
        startBuffer()
    } else {
        clearInterval(myinterval)
        console.log('finished!')
    }
}


// create a timer that will trigger emptying buffer after 2s
const myinterval = setInterval(()=>{
    console.log('time out!')
    timeoutNotPassed = false
}, 3000)
startBuffer()