column_list = {
  "work_id": false,
  "student_initials": true,
  "student_grp": true,
  "student_course": false,
  "student_dept": false,
  "student_faculty": false,
  "advisor_initials": true,
  "advisor_dept": false,
  "advisor_faculty": false,
  "written_in": true,
  "field_of_study": true,
  "theme": true,
  "file_link": false
};

var dropdown_state = false;
  
advisor_dict = {};
student_dict = {};
coursework_dict = {};


// GUI FUNCTIONS
function openNav() {
    document.getElementById("myNav").style.width = "100%";
}

function closeNav() {
    document.getElementById("myNav").style.width = "0%";
}

function openNav2() {
  document.getElementById("myNav2").style.width = "100%";
}

function closeNav2() {
  document.getElementById("myNav2").style.width = "0%";
}

function toggle_dropdown() {
  dropdown_state = !dropdown_state;
  var content = document.getElementById("dropdown-content")
  content.style.display = dropdown_state ? '' : 'none'
}

function alter_visibility(key) {
  id = key + '-checkbox';
  column_list[key] = document.getElementById(id).checked;
  refresh_table_visibility();
}


function refresh_table_visibility() {
  for (let [key, value] of Object.entries(column_list)) {
    var items = document.getElementsByClassName(key);
    for (i = 0; i < items.length; i++) {
      items[i].style.display = value ? '' : 'none'
    }
  }

  var res = document.querySelector('#main_table').clientWidth - 50;
  document.getElementById('dropdown_div').style.transform = 'translate('+res +'px, 0)';

  var anchors = document.getElementsByTagName('td');
  for(var i = 0; i < anchors.length; i++) {
      var anchor = anchors[i];
      anchor.onclick = function(event) {
        var obj = event.target;
        fetch_db(obj.className, obj.textContent);
      };
  }
  var anchors = document.getElementsByTagName('th');
  for(var i = 0; i < anchors.length; i++) {
    var anchor = anchors[i];
    anchor.onclick = function(event) {
      var obj = event.target;
      var is_asc = true;
      fetch_db('', '', obj.className);
    };
  }
}

function add_lst(){
  document.onkeydown = function(evt) {
      evt = evt || window.event;
      var isEscape = false;
      if ("key" in evt) {
          isEscape = (evt.key === "Escape" || evt.key === "Esc");
      } else {
          isEscape = (evt.keyCode === 27);
      }
      if (isEscape) {
          closeNav();
          closeNav2();
      }
  };
}



// DATA PROCESSING FUNCTIONS
function populate_student_dict(data) {
  data = JSON.parse(data);
  student_dict = data;
  let placeholder = document.querySelector("#student_optgroup");
  let out = "";
  for (let [key, value] of Object.entries(data)) {
    out += `
            <option value='${key}'>${value}</option>
        `;
  }
  placeholder.innerHTML = out;
}

function populate_advisor_dict(data) {
  data = JSON.parse(data);
  advisor_dict = data;
  let placeholder = document.querySelector("#advisor_optgroup");
  let out = "";
  for (let [key, value] of Object.entries(data)) {
    out += `
            <option value='${key}'>${value}</option>
        `;
  }
  placeholder.innerHTML = out;
}


function update_table(data) {
  data = JSON.parse(data);
  let placeholder = document.querySelector("#data_output");
  let out = "";
  for (let row of data) {
    coursework_dict[row['work_id']] = row['theme'];
    out += "<tr>"
    var cl = Object.keys(column_list)
    for (var i = 0; i < cl.length; i++) {
      if (row[cl[i]] === undefined || row[cl[i]]==null) {
        out += `
                    <td class='${cl[i]}'  ${column_list[cl[i]]?'':'style=\"display: none;\"'}>—</td>
                `;
      } else {
        out += `
                    <td class='${cl[i]}' ${column_list[cl[i]]?'':'style=\"display: none;\"'}>${row[cl[i]]==''?'—':row[cl[i]]}</td>
                `;
      }
    }
    out += "</tr>"
  }

  placeholder.innerHTML = out;
  refresh_table_visibility();

  let ph = document.querySelector("#coursework_optgroup");
  let output = "";
  for (let [key, value] of Object.entries(coursework_dict)) {
    output += `
            <option value='${key}'>${key} - ${value}</option>
        `;
  }
  ph.innerHTML = output;
}
