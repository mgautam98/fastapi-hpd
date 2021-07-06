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
            toggleEditOverlay()
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
            toggleCreateOverlay()
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
    header.children[0].id = data.providerID

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
    qualification.children[1].children[0].value = data.qualification.join(', ')

    speciality = document.querySelector('#edit-overlay').childNodes[1].children[3]
    speciality.children[1].children[0].value = data.speciality.join(', ')

    phone = document.querySelector('#edit-overlay').childNodes[1].children[4]
    phone.children[1].children[0].value = data.phone.join(', ')
}

const submitEditRecord = () => {
    // TODO: Check for null values
    var providerID = document.querySelector('#edit-overlay').childNodes[1].children[0].children[0].id
    var name = document.querySelector('#edit-overlay').childNodes[1].children[1].children[1].children[0].value
    var department = document.querySelector('#edit-overlay').childNodes[1].children[5].children[1].children[0].value
    var organization = document.querySelector('#edit-overlay').childNodes[1].children[6].children[1].children[0].value
    var location = document.querySelector('#edit-overlay').childNodes[1].children[7].children[1].children[0].value
    var address = document.querySelector('#edit-overlay').childNodes[1].children[8].children[1].children[0].value
    var qualification = document.querySelector('#edit-overlay').childNodes[1].children[2].children[1].children[0].value
    var speciality = document.querySelector('#edit-overlay').childNodes[1].children[3].children[1].children[0].value
    var phone = document.querySelector('#edit-overlay').childNodes[1].children[4].children[1].children[0].value

    qualification = qualification.split(',').map(x => x.replace(/^\s/g, ''))
    speciality = speciality.split(',').map(x => x.replace(/^\s/g, ''))
    phone = phone.split(',').map(x => x.replace(/^\s/g, ''))

    var data = {
        name: name ? name : null,
        department: department ? department : null,
        organization: organization ? organization : null,
        location: location ? location : null,
        address: address ? address : null,
        qualification: qualification ? qualification : null,
        speciality: speciality ? speciality : null,
        phone: phone ? phone : null,
    }
    editRecord(providerID, data)
}

const submitCreateRecord = () => {
    // TODO: Check for null values
    var name = document.querySelector('#create-overlay').childNodes[1].children[1].children[1].children[0].value
    var department = document.querySelector('#create-overlay').childNodes[1].children[5].children[1].children[0].value
    var organization = document.querySelector('#create-overlay').childNodes[1].children[6].children[1].children[0].value
    var location = document.querySelector('#create-overlay').childNodes[1].children[7].children[1].children[0].value
    var address = document.querySelector('#create-overlay').childNodes[1].children[8].children[1].children[0].value
    var qualification = document.querySelector('#create-overlay').childNodes[1].children[2].children[1].children[0].value
    var speciality = document.querySelector('#create-overlay').childNodes[1].children[3].children[1].children[0].value
    var phone = document.querySelector('#create-overlay').childNodes[1].children[4].children[1].children[0].value

    qualification = qualification.split(',').map(x => x.replace(/^\s/g, ''))
    speciality = speciality.split(',').map(x => x.replace(/^\s/g, ''))
    phone = phone.split(',').map(x => x.replace(/^\s/g, ''))

    var data = {
        name: name ? name : null,
        department: department ? department : null,
        organization: organization ? organization : null,
        location: location ? location : null,
        address: address ? address : null,
        qualification: qualification ? qualification : null,
        speciality: speciality ? speciality : null,
        phone: phone ? phone : null,
    }
    // console.log(data)
    createRecord(data)
}

const successToast = (message, time = 3000) => {
    toast = document.getElementById('toast')
    success = document.getElementById('success-toast')
    success_msg = document.getElementById('success-toast-msg')

    success_msg.textContent = message
    toast.classList.remove('hidden')
    success.classList.remove('hidden')
    success.classList.add('flex')

    setTimeout(() => {
        success.classList.remove('flex')
        success.classList.add('hidden')
        toast.classList.add('hidden')
    }, time)
}

const infoToast = (message, time = 3000) => {
    toast = document.getElementById('toast')
    info = document.getElementById('info-toast')
    info_msg = document.getElementById('info-toast-msg')

    info_msg.textContent = message
    toast.classList.remove('hidden')
    info.classList.remove('hidden')
    info.classList.add('flex')

    setTimeout(() => {
        info.classList.remove('flex')
        info.classList.add('hidden')
        toast.classList.add('hidden')
    }, time)
}

const errorToast = (message, time = 3000) => {
    toast = document.getElementById('toast')
    error = document.getElementById('error-toast')
    error_msg = document.getElementById('error-toast-msg')

    error_msg.textContent = message
    toast.classList.remove('hidden')
    error.classList.remove('hidden')
    error.classList.add('flex')

    setTimeout(() => {
        error.classList.remove('flex')
        error.classList.add('hidden')
        toast.classList.add('hidden')
    }, time)
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