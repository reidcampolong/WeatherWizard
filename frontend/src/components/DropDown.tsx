import React from 'react';
import cities from '../cities';
import Select from 'react-select';
interface IDropDown {
  readonly placeholder: string;
  readonly setDropDownSelect: React.Dispatch<React.SetStateAction<string>>;
}

const DropDown: React.SFC<IDropDown> = ( {placeholder, setDropDownSelect} ) => {

  const handleOnChange = (e: any) => {
    setDropDownSelect(e.value);
  };

  return (
    <Select 
      placeholder={placeholder}
      onChange={handleOnChange}
      options={cities.map(city => ({ label: city, value: city }))} />
  );
};

export default DropDown;