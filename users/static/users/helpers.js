const isStudent = () => {
  const isStudentSection = document.querySelector(".is_student")
  const isStaffCheckbox = document.querySelector("#id_is_staff")

  if (isStaffCheckbox.checked === true) isStudentSection.classList.add("d-none")
  else isStudentSection.classList.remove("d-none")
}
