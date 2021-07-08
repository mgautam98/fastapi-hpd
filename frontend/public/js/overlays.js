
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
    createRecord(data)
}


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
