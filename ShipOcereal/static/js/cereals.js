$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault()
        var searchText = $('#search-bar').val();
        $.ajax( {
            url: '?search_filter='+searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="singleCerealContainer">
                                <a href="/${d.id}">
                                    <img class="cereal-img" src="${d.image}"/>
                                    <h4>${d.name}</h4>
                                    <p>${d.description}</p>
                                </a>
                            </div>`
                });
                $('.Cereals').html(newHtml.join(''));
                $('#searchbar').val('');
            },
            error: function(xhr, status, error){
                console.error(error);
                //TODO: show better error message
            }
        })
    });
});
