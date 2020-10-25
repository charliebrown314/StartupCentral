function newRecommendationTile(name, desc_txt, img_URL){
    let tile = document.createElement('div')
    let tile_name = document.createElement('div')
    let desc = document.createElement('div');
    let hr = document.createElement('hr')
    let img = document.createElement('img');
    tile.className = 'row-tile recommendation tile-clickable';
    tile_name.className = 'tile-name';
    tile_name.innerText = name;
    desc.className = 'recommendation-desc'
    desc.innerText = desc_txt
    img.src = img_URL;
    tile.append(tile_name,hr,desc,img)
    return tile;
}

function newColTile(name, tags, img_URL ){
    let tile = document.createElement('div');
    let wrapper = document.createElement('div');
    let tile_name = document.createElement('div');
    let tag_container = document.createElement('div');
    let tag1 = document.createElement('div');
    let tag2 = document.createElement('div');
    let tag3 = document.createElement('div');
    let img = document.createElement('img');
    tile.className = 'col-tile nameplate tile-clickable';
    tile_name.className = 'tile-name';
    tile_name.innerText = name
    tag_container.className = 'nameplate-tags';
    tag1.className = 'tag';
    tag1.innerText = tags[0];
    tag2.className = 'tag';
    tag2.innerText = tags[1];
    tag3.className = 'tag';
    tag3.innerText = tags[2];
    img.src = img_URL;
    tag_container.append(tag1,tag2,tag3,document.createTextNode('...'));
    wrapper.append(tile_name,tag_container);
    tile.append(wrapper,img);
    return tile;
}

function newSearchResult(name, desc, tags, collabs, img_URL){
    let result = document.createElement('div')
    let r_name = document.createElement('div')
    let wrapper = document.createElement('div')
    let r_desc = document.createElement('div')
    let tag_container = document.createElement('div')
    let col_header = document.createElement('h3')
    let col_container = document.createElement('div')
    let img_wrap = document.createElement('div')
    let img = document.createElement('img')
    result.className = 'search-result'
    r_name.className = 'search-result-name'
    r_name.innerText = name
    wrapper.className = 'search-tag-result-wrapper'
    r_desc.className = 'search-result-desc'
    r_desc.innerText = desc
    tag_container.className = 'search-result-tags'
    loadPageTags(tags, tag_container)
    col_header.innerText = 'Collaborators'
    col_container.className = 'search-result-collabs'
    loadPageTags(collabs, col_container)
    img_wrap.className = 'search-img-wrapper'
    img.src = img_URL
    wrapper.append(r_desc,tag_container,col_header,col_container)
    img_wrap.appendChild(img_wrap)
    result.append(r_name,wrapper,img_wrap)
    return result
}

function loadPageTags(tags, container){
    for (tag of tags){
        let div = document.createElement('div')
        div.className = 'tag'
        div.innerText = tag
        container.appendChild(div)
    }
}