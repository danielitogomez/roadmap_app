document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.roadmap-item').forEach(function(item) {
        item.addEventListener('click', function() {
            var dataLinks = JSON.parse(this.getAttribute('data-links').replace(/&quot;/g, '\"'));
            //console.log(dataLinks);  // Check what dataLinks contains after parsing
            openSidebar(dataLinks);
        });
    });
});

function openSidebar(links) {
    var linkList = document.getElementById("linkList");
    linkList.innerHTML = "";  // Clear current links

    links.forEach(function(link) {
        var anchor = document.createElement('a');
        anchor.href = link.url;
        anchor.target = "_blank";
        anchor.textContent = link.name;
        linkList.appendChild(anchor);
    });

    document.getElementById("sidebar").style.width = "300px";
}

function closeSidebar() {
    document.getElementById("sidebar").style.width = "0";
}
