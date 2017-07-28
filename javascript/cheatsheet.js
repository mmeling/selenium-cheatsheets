// DRIVER STUFF
// todo later

// GO TO URL
browser.url('PATH');


// PAGE OBJECT WEBELEMENT
get elementName() { return browser.element('locator'); }


// FINDING ELEMENTS
browser.element('locator');
// some of the actions can do the search for you
browser.click('locator');
browser.getText('locator');


// WAIT FOR ELEMENTS
this.element.waitForEnabled();
this.element.waitForExist();
this.element.waitForSelected();
this.element.waitForText();
this.element.waitForValue();
this.element.waitForVisible();
this.element.waitUntil();


// ASSERTIONS
// asserting seems to be done through expectations
expect(selector).to.be.there();
expect(selector).to.be.visible();
expect(selector).to.have.text('TEXT');
expect(selector).to.have.text(/regex/);
expect(selector).to.have.count(int);
expect(selector).to.contain('TEXT');
// negate the assertion with .not
expect(selector).not.to.contain('TEXT')


// EXECUTE JS
browser.execute(function(arg) {'script'}, arg);
// hide element
document.getElementById('id').style.display = 'none';
document.getElementByClassName('class').style.display = 'none';
document.getElementByName('name').style.display = 'none';
document.evaluate ('path', document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue.style.display = 'none';
// remove element
document.getElementById('id').remove();
document.getElementByClassName('class').remove();
document.getElementByName('name').remove();
document.evaluate('path', document, null, XPathResult.FIRSTORDERED_NODE_TYPE,null).singleNodeValue.remove();


// SELECT BOXES
select.selectByAttribute('ATTRIBUTE');
select.selectByIndex(index);
select.selectByVisibleText('TEXT');
select.selectByValue('VALUE');
// get value
var options = select.getValue();


// CLICK ELEMENT
element.click();


// FILL TEXT FIELD
element.setValue('TEXT');


// CHECK AND UNCHECK CHECK BOXES
// to see if checked or not
element.isSelected();
// to check
if(element.isSelected()) {
    browser.click(element);
};
// to uncheck
// though this doesn't work if the element is null or undefined
if(!element.isSelected()) {
    browser.click(element);
};


// FIND IF ELEMENT EXISTS IN DOM
if(element.isExisting()){
    // element exists
};

// GET TEXT FROM ELEMENT
element.getText();

// UPLOAD A FILE
browser.chooseFile(element,'PATH');

# ALERTS
driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()


// RANDOM DRIVER ELEMENTS
browser.getUrl();
browser.delete_cookie();
