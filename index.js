function saturdayFun(activity="roller-skate"){
    return `This saturday, i want to ${activity}`
}

// console.log(saturdayFun("roller-skate with brandi"));

// (() => console.log(`This saturday, i want to`))()
// const catFunc = cat => console.log(`This saturday, i want to ${cat}`)
// catFunc("cat")


const options ={
    method : "GET",
    mode: 'cors',
    headers : {
        "Authorization":"kZLIYkxusXzOsvUbw9OAZaadOKSuJVzhvnHgS2oJOXAcUQ8kzZUn4uVo",
    }
}

async function imageQuery(query) {
    const response = await fetch(`https://api.pexels.com/v1/search?query=${query}`,options);
    const images = await response.json();
    console.log(images);
    return images;
}

imageQuery("cat")