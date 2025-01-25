import React, { useEffect, useState } from 'react'
import axios from 'axios'

const Home = () => {
    const[category, setCategory] = useState([])
    useEffect(()=>{
        axios.get(`http://127.0.0.1:8000/app/allcategory/`)
        .then(
            res=>setCategory(res.data)
        )
        .catch(err=>console.log(err))
    })
  return (
    <>
    <h1>{category.category_name}</h1>
    </>
  )
}

export default Home