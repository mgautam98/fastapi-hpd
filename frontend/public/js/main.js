async function init() {
    await getAllRecords()
}


/**
 * Limit and skip counter
 * */
var skipG = 0
const limitG = 10


/**
 * Get all records
 * called from index.html
 * 
 * @param {bool} prev - if true, get previous records
 * */
async function getResults(prev = false) {
    if (prev) {
        skipG = skipG - limitG < 0 ? 0 : skipG - limitG
    } else {
        skipG += limitG
    }
    return getAllRecords(skipG, limitG)
}


/**
 * fetches all the records from server
 * 
 * @param {int} skip - records to skip
 * @param {int} limit - total records to return
 * */
async function getAllRecords(skip = 0, limit = 10) {
    await clearResults()
    fetch(`/api/provider/?skip=${skipG}&limit=${limitG}`)
        .then(response => {
            if (response.status != 200) {
                console.log(response)
                return
            }
            response.json().then(data => {
                data = data.map(addRow)
                data.map(addToTable)
                return
            })
        })
        .catch(err => console.log(err))
}


/**
 * Gets a single record from server
 * @param {int} id - record id
 * */
const getRecord = (id => {
    axios.get(`/api/provider/${id}`)
        .then(response => {
            if (response.status != 200) {
                console.log(response)
                return
            }
            addDataToShowOverlay(response.data)
            toggleShowOverlay()
        })
        .catch(error => console.error(error))
})


/**
 * Edit a record
 * @param {int} id - record id
 * @param {object} data - data to be edited
 * */
const editRecord = (id, data) => {
    axios.put(`/api/provider/${id}`, data)
        .then(response => {
            if (response.status != 204) {
                console.log(response)
                return
            }
            getRecord(id)
        })
        .catch(error => console.error(error))
}

/**
 * Show and edit record
 * @param {int} id - record id
 * */
const getRecordAndEdit = (id) => {
    axios.get(`/api/provider/${id}`)
        .then(response => {
            if (response.status != 200) {
                console.log(response)
                return
            }
            addDataToEditOverlay(response.data)
            toggleEditOverlay()
        })
        .catch(error => console.error(error))
}

/**
 * Create record
 * @param {object} data - data to be posted
 * */
const createRecord = (data) => {
    axios.post('/api/provider', data)
        .then(response => {
            if (response.status != 201) {
                console.log(response)
                return
            }
        })
        .catch(error => console.error(error))
}


/**
 * Deletes a record from server
 * @param {int} id - record id
 * */
const deleteRecord = (id => {
    axios.delete(`/api/provider/${id}`)
        .then(response => {
            if (response.status != 200) {
                console.log(response)
                return
            }
        })
        .then(() => {
            document.getElementById(id).remove()
        })
        .catch(error => console.error(error))
})


/**
 * Adds a row to the results table
 * called from getAllRecords
 * 
 * @param {object} data - data to be added to the table
 * */
const addRow = (data => {
    // TODO: adjust size of org and qual
    tr = document.createElement("tr")
    tr.classList.add("table-row")
    tr.id = data.providerID

    name_ = document.createElement("td")
    name_.classList.add("table-item")
    name_.textContent = data.name
    tr.appendChild(name_)

    org = document.createElement("td")
    org.classList.add("table-item")
    org.textContent = data.organization.length <= 20 ? data.organization : data.organization.substring(0, 20) + "..."
    tr.appendChild(org)

    qual = document.createElement("td")
    qual.classList.add("table-item")
    qual.textContent = data.qualification[0].length <= 15 ? data.qualification[0] : data.qualification[0].substring(0, 15) + "..."
    tr.appendChild(qual)

    operations = document.createElement("td")
    operations.classList.add("table-item")

    operations.innerHTML = `
    <a href="#" onClick="getRecord(this.parentNode.parentNode.id)" class="table-button button-view" id="show-btn">
        View</a>
    <a href="#" onClick="getRecordAndEdit(this.parentNode.parentNode.id)" class="table-button button-edit">
        Edit</a>
    <a href="#" onClick="deleteRecord(this.parentNode.parentNode.id)" class="table-button button-delete">
        Delete</a>
    `

    tr.appendChild(operations)

    return tr
})


/**
 * Helper function to clear table
 * */
async function clearResults() {
    results = await document.getElementById("results")
    var tableHeaderRowCount = 0;
    var rowCount = results.rows.length;
    for (var i = tableHeaderRowCount; i < rowCount; i++) {
        results.deleteRow(tableHeaderRowCount);
    }
}


/**
 * Helper function to add each row to table
 * @param {object} row - row to be added to the table
 * */
const addToTable = (row => {
    results = document.getElementById("results")
    results.appendChild(row)
})

/**
 * Add data to show Overaly dynamically
 * @param {object} data - data to be added to the overlay
 * */
const addDataToShowOverlay = (data) => {
    header = document.querySelector('#show-overlay').childNodes[1].children[0]
    header.children[0].textContent = data.name


    department = document.querySelector('#show-overlay').childNodes[1].children[4]
    if (data.department) {
        department.children[1].textContent = data.department
    } else {
        department.children[1].textContent = "N/A"
    }

    loc = document.querySelector('#show-overlay').childNodes[1].children[6]
    if (data.location) {
        loc.children[1].textContent = data.location
    } else {
        loc.children[1].textContent = "N/A"
    }

    org = document.querySelector('#show-overlay').childNodes[1].children[5]
    org.children[1].textContent = data.organization


    address = document.querySelector('#show-overlay').childNodes[1].children[7]
    address.children[1].textContent = data.address

    qual = document.querySelector('#show-overlay').childNodes[1].children[1]
    qual.children[1].textContent = ''
    for (quals in data.qualification) {
        span = document.createElement("span")
        span.textContent = data.qualification[quals]
        qual.children[1].appendChild(span)
    }

    speciality = document.querySelector('#show-overlay').childNodes[1].children[2]
    speciality.children[1].textContent = ''
    for (specialities in data.speciality) {
        span = document.createElement("span")
        span.textContent = data.speciality[specialities]
        speciality.children[1].appendChild(span)
    }

    phone = document.querySelector('#show-overlay').childNodes[1].children[3]
    phone.children[1].textContent = ''
    for (phones in data.phone) {
        span = document.createElement("span")
        span.textContent = data.phone[phones]
        phone.children[1].appendChild(span)
    }
}

const addDataToEditOverlay = (data) => {
    header = document.querySelector('#edit-overlay').childNodes[1].children[0]
    header.children[0].textContent = data.name

    name_ = document.querySelector('#edit-overlay').childNodes[1].children[1]
    name_.children[1].children[0].value = data.name

    department = document.querySelector('#edit-overlay').childNodes[1].children[5]
    department.children[1].children[0].value = data.department

    org = document.querySelector('#edit-overlay').childNodes[1].children[6]
    org.children[1].children[0].value = data.organization

    loc = document.querySelector('#edit-overlay').childNodes[1].children[7]
    loc.children[1].children[0].value = data.location

    address = document.querySelector('#edit-overlay').childNodes[1].children[8]
    address.children[1].children[0].value = data.address

    qualification = document.querySelector('#edit-overlay').childNodes[1].children[2]
    qualification_str = ""
    for (quals in data.qualification) {
        qualification_str += data.qualification[quals] + ","
    }
    qualification.children[1].children[0].value = qualification_str

    speciality = document.querySelector('#edit-overlay').childNodes[1].children[3]
    speciality_str = ""
    for (specialities in data.speciality) {
        speciality_str += data.speciality[specialities] + ","
    }
    speciality.children[1].children[0].value = speciality_str

    phone = document.querySelector('#edit-overlay').childNodes[1].children[4]
    phone_str = ""
    for (phones in data.phone) {
        phone_str += data.phone[phones] + ","
    }
    phone.children[1].children[0].value = phone_str
}


/**
 * Toggles the show overlay
 * */
const toggleShowOverlay = () => {
    document.getElementById('show-overlay').classList.toggle('hidden');
    document.getElementById('show-overlay').classList.toggle('flex');
}

const toggleEditOverlay = () => {
    document.getElementById('edit-overlay').classList.toggle('hidden');
    document.getElementById('edit-overlay').classList.toggle('flex');
}

const toggleCreateOverlay = () => {
    document.getElementById('create-overlay').classList.toggle('hidden');
    document.getElementById('create-overlay').classList.toggle('flex');
}


/* Initialize DOM */
init()