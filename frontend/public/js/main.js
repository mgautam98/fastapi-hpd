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
        .catch(error => errorToast(error))
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
                errorToast(response.detail)
                return
            }
            toggleEditOverlay()
            successToast('Record Saved Successfully!')
        })
        .catch(error => errorToast(error.details))
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
        .catch(error => errorToast(error))
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
            successToast('Record Created Successfully!')
        })
        .catch(error => errorToast(error))
}


/**
 * Deletes a record from server
 * @param {int} id - record id
 * */
const deleteRecord = (id => {
    axios.delete(`/api/provider/${id}`)
        .then(response => {
            if (response.status != 204) {
                errorToast(response.detail)
                return
            }
            successToast('Record Deleted Successfully!')
        })
        .then(() => {
            document.getElementById(id).remove()
        })
        .catch(error => errorToast(error))
})


/* Initialize DOM */
init()