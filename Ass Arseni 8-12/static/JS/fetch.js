console.log('inside fetch example')


function getUsers(user_id_front){
    console.log('clicked');
    fetch('https://reqres.in/api/users').then(
        response => response.json()
    ).then(
        response_obj => put_id_inside_html(response_obj.data.user_id_front)
    ).catch(
        err => console.log(err)
    )
}

function put_id_inside_html(response_obj_data,user_id_front) {
    // console.log(response_obj_data);

    const curr_main = document.querySelector("main");
    for (let user of response_obj_data) {
      if (user.id == user_id_front)
        const section = document.createElement('section');
        section.innerHTML = `
        <img src="${user.avatar}" alt="Profile Picture"/>
        <div>
            <span>${user.first_name} ${user.last_name}</span>
            <br>
            <a href="mailto:${user.email}">Send Email</a>
        </div>
        `;
        curr_main.appendChild(section);
    }
}