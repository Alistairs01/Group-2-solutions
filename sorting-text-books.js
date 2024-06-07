/**
 * function sorter(textbooks) {

    return textbooks.sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
}
 */

function sorter(textbooks) {
    // Custom sorting algorithm without using built-in methods
    for (let i = 0; i < textbooks.length - 1; i++) {
        for (let j = i + 1; j < textbooks.length; j++) {
            if (compareStringsIgnoreCase(textbooks[i], textbooks[j]) > 0) {
                // Swap elements if they are in the wrong order
                const temp = textbooks[i];
                textbooks[i] = textbooks[j];
                textbooks[j] = temp;
            }
        }
    }

    return textbooks;
}

function compareStringsIgnoreCase(str1, str2) {
    // Compare strings character by character in a case-insensitive manner
    const minLength = Math.min(str1.length, str2.length);
    for (let i = 0; i < minLength; i++) {
        const charCode1 = str1.charCodeAt(i);
        const charCode2 = str2.charCodeAt(i);

        // Convert characters to lowercase for comparison
        const lowerCharCode1 = (charCode1 >= 65 && charCode1 <= 90) ? charCode1 + 32 : charCode1;
        const lowerCharCode2 = (charCode2 >= 65 && charCode2 <= 90) ? charCode2 + 32 : charCode2;

        if (lowerCharCode1 !== lowerCharCode2) {
            // If characters are not equal, return the comparison result
            return lowerCharCode1 - lowerCharCode2;
        }
    }

    // If one string is a prefix of the other, the shorter string should come first
    return str1.length - str2.length;
}

module.exports = sorter;
