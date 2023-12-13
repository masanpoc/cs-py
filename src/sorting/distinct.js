function distinct(array) {
    array.sort()
    unique_sum=1
    array.forEach((value, idx) =>{
        if(idx!=0 && array[idx]!=array[idx-1]){
                unique_sum +=1
        }
    })
    return unique_sum
}

console.log(distinct([1,1,2,1,1,2]))