$(document).ready(function(){
    //Search button clicked @ home Page
    $('#searchWord').on('click',function(){
       
        //move to search page 
       location.replace(`search?word=${$('#choices-text-preset-values').val()}`)
    })


    
})
