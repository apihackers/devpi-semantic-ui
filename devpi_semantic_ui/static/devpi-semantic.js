$(function() {

    // Tooltips
    $('.icon.tooltip').popup();

    $('.ui.search').search({
        type: 'category',
        minCharacters : 3,
        apiSettings: {
            beforeXHR: function(xhr) {
                xhr.setRequestHeader('Accept', 'application/json');
                xhr.setRequestHeader('Content-Type', 'application/json');
                return xhr;
            },
            onResponse: function(devpiResponse) {
                var response = {results : {}};

                // translate devpi API response to work with search
                $.each(devpiResponse.result.items, function(index, item) {
                    var branch = item.data.user + '/' + item.data.index;
                    // create new language category
                    if(response.results[branch] === undefined) {
                        response.results[branch] = {
                            name    : '<i class="icon fork"></i>' + branch,
                            results : []
                        };
                    }
                    response.results[branch].results.push({
                        title: item.title,
                        url: item.url,
                    });
                });

                if (devpiResponse.result.info.pagecount > 1) {
                    response.action = {
                        url: '/+search?query=' + devpiResponse.result.query,
                        "text": 'View all '+ devpiResponse.result.info.total +' results'
                    };
                }

                return response;
            },
            url: '/+search?query={query}'
        },
  });

})
