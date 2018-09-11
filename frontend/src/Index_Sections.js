import React, { Component } from 'react';
import Section_Features from './Section_Features';

class Index_Sections extends Component {
  render() {
    return (
      <div className="index_sections">
      {this.props.sections.map(
        section => 
        <Section_Features section={section}/>
      )} 
      </div>
    );
  }
}

export default Index_Sections;