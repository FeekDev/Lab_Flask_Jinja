/* Poner imagenes en el footer de un documento */
function myFunction() {
    // get the document blob
    var doc = DocumentApp.getActiveDocument();
  
  // Get an image in Drive from its ID.
  var image = DriveApp.getFileById('1ExhccLUCfYqDVycvOqAUb2-SBmvso35U');
  
  doc.addFooter().appendImage(image)
  
  }